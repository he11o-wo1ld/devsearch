// //Get Search Form and Page Link
// let searchForm = document.getElementById('searchForm');
// let pageLink = document.getElementsByClassName('page-link');
//
// //Ensure Search Form Exists
// if(searchForm){
//   for(let i=0; pageLink.length > i; i++){
//     pageLink[i].addEventListener('click', function (e){
//       e.preventDefault();
//
//       // Get The Data Attributes
//       let page = this.dataset.page
//
//       // Add Hidden Search To Input Form
//       searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
//
//       // Submit Form
//       searchForm.submit()
//
//     });
//   }
// }


//GET SEARCH FORM AND PAGE LINKS
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

//ENSURE SEARCH FORM EXISTS
if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function (e){
            e.preventDefault()

            // Get The Data Attributes
            let page = this.dataset.page

            // Add Hidden Search To Input Form
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`


            //SUBMIT FORM
            searchForm.submit()
        })
    }
}
