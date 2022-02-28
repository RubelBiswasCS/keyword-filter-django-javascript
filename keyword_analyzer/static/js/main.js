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
                keywordList.innerHTML += `<li>${item.name} ( found ${item.count} times) </li>`
            });

        })
    }
    
}

const filterKeywords = (keywords) => {
    //console.log(keywords)
    const checkboxs = document.getElementsByClassName('checkbox');

    console.log(checkboxs)
    var checkedIds = []
    for (let i of checkboxs){
        console.log(i.checked)
        if(i.checked){
            checkedIds = [...checkedIds, i.id]
        }
        
    }
   console.log(checkedIds)
    return keywords.filter( (keyword) => {
        return keyword.search_history.some((i) => {
            console.log(i.user.id)
            if(checkedIds.includes(i.user.id.toString())){
                return true;
            }
        })
    })

}