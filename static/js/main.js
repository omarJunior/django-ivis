let searchForm = document.getElementById("searchForm")
let pageLinks = document.querySelectorAll(".page-link")
//ensure search form exists
if(searchForm){
    for(let i= 0; i < pageLinks.length; i++){
        pageLinks[i].addEventListener('click', (e)=>{
            e.preventDefault()
            let page = e.target.dataset.page
            searchForm.innerHTML += `<input value=${page} name="page" hidden />`
            searchForm.submit()
        })
    }
}
