// alert('js loaded !!')
const testAlert = (value) => {
    console.log('js loaded, value: ',value)
    alert('js loaded')
}

function getCheckboxs(keywords){
    
    const checkboxs = document.getElementsByClassName('checkbox');
    const keywordList = document.getElementsByClassName('keywords-list')[0]
    for(let i of checkboxs){
        console.log(i.name+' '+i.checked)
        //console.log(i)
        i.addEventListener( 'change' , () => {
            console.log('changed')
            let filteredKeywords = filterKeywords(keywords)
            console.log(filteredKeywords)
            keywordList.innerHTML=''
            filteredKeywords.forEach(item => {
                //console.log(item)
                keywordList.innerHTML += `<li>${item.keyword} | ${item.user} | ${item.search_date}</li>`
            });

        })
    }
    
}

const filterKeywords = (keywords) => {
    //console.log(keywords)
    return keywords.filter( (keyword) => {
        let currentCheckbox = document.getElementById(keyword.user)
        //console.log(currentCheckbox)
        if (currentCheckbox.checked){
            return true;
        }
    })
}