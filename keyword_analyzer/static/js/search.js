
const clearBtn=document.getElementById("clear")
const textBox=document.getElementById("search-text")
// console.log(clearBtn,textBox)
if(textBox.value===''){
    clearBtn.style.visibility = 'hidden';
}
textBox.addEventListener('input',()=> {
    if(textBox.value===''){
        clearBtn.style.visibility = 'hidden';
    }
    else{
        clearBtn.style.visibility = 'visible';
    }
})
const handleClearBtnClick = (e) => {
    e.preventDefault();
    textBox.value='';
    clearBtn.style.visibility = 'hidden';
}
clearBtn.addEventListener('click',handleClearBtnClick)

