const testAlert = (value) => {
    console.log('js loaded, value: ', value)
    alert('js loaded')
}

function handleFilters(keywords) {

    const checkboxs = document.getElementsByClassName('checkbox');
    const countBasedCheckboxs = document.getElementsByClassName('count');
    const dateBasedCheckboxs = document.getElementsByClassName('date');

    const keywordList = document.getElementsByClassName('keywords-list')[0]
    const customDates = document.getElementsByClassName('custom-date-input')

    const updateUi = (keywords) => {
        let filteredKeywords = filterKeywords(keywords)
        //console.log(filteredKeywords)
        keywordList.innerHTML = ''
        filteredKeywords.forEach((item, i) => {
            keywordList.innerHTML += `<li>${i + 1}. ${item.name} ( found ${item.count} times) </li>`
        });
    }
    for (let i of checkboxs) {
        i.addEventListener('change', () => {
            updateUi(keywords)
        })
    }
    for (let i of customDates) {
        i.addEventListener("input", (e) => {
            updateUi(keywords);
        })
    }

    for (let i of countBasedCheckboxs) {
        i.addEventListener('click', (e) => {
            let target = e.target
            for (let c of countBasedCheckboxs) {
                c.checked = false
            }
            target.checked = true
        })
    }

    for (let i of dateBasedCheckboxs) {
        i.addEventListener('click', (e) => {
            let target = e.target
            for (let c of dateBasedCheckboxs) {
                c.checked = false
            }
            target.checked = true
        })
    }

}

//filter keywords based on count
const filterByCount = (keywords) => {
    const countCheckboxes = document.getElementsByClassName('count')
    let count = 0
    let value;
    for (let i of countCheckboxes) {
        if (i.checked) {
            value = i.id
            count += 1
        }
    }
    if (value === 'count1' || count === 0) {
        return keywords;
    }
    return keywords.filter(keyword => {
        return keyword.count >= parseInt(value.slice(5, value.length))
    })
}

//filtr by searching date
const filterByDate = (keywords) => {
    let today = new Date();
    const dateCheckboxes = document.getElementsByClassName('date')
    let value;
    let count = 0;
    for (let i of dateCheckboxes) {
        if (i.checked) {
            value = i.id
            count += 1
        }
    }
    if (value === 'anytime' || count === 0) {
        return keywords;
    }

    //filter for custom date input
    else if (value === 'custom-date') {
        const startDate = document.getElementById('start-date').value
        const endDate = document.getElementById('end-date').value
        if (startDate === "" || endDate === "") {
            return keywords;
        }
        return keywords.filter(keyword => {
            return keyword.search_history.some(i => {
                var date = i.search_date.slice(0, 10)

                if (date >= startDate && date <= endDate) {
                    return true
                }
            });
        });
    }
    else {
        switch (value) {
            case 'day':
                day = 1;
                break;
            case 'week':
                day = 7;
                break;
            case 'month':
                day = 30;
                break;

        }

        return keywords.filter(keyword => {
            return keyword.search_history.some(i => {
                var form_date = new Date(i.search_date.slice(0, 10))
                var difference = form_date > today ? form_date - today : today - form_date
                var diff_days = Math.floor(difference / (1000 * 3600 * 24))
                //console.log(diff_days)

                if (diff_days <= day) {
                    return true
                }
            })
        })
    }

}

const filterKeywords = (keywords) => {
    const checkboxs = document.getElementsByClassName('by-user');
    var checkedIds = []
    for (let i of checkboxs) {
        if (i.checked) {
            checkedIds = [...checkedIds, i.id]
        }
    }
    var keywords = filterByCount(keywords)
    var keywords = filterByDate(keywords)
    if (checkedIds.length === 0) {
        return keywords;
    }
    //filter based on user
    const filteredKeywords = keywords.filter((keyword) => {
        return keyword.search_history.some((i) => {

            if (checkedIds.includes(i.user.id.toString())) {
                return true;
            }
        })


    })

    return filteredKeywords;
}