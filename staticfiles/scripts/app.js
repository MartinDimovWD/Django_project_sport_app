const dashboardNavLinks =
        Array.from(document.getElementsByClassName('dashboard-nav-link'))
const dashboardSections =
    Array.from(document.getElementsByClassName('dashboard-section'))

function hideSections(){
    dashboardSections.forEach(section=>section.style.display='none')
}
hideSections()
dashboardSections[0].style.display='block'
function showSectionOnNavClick(navBtn){

    let navBtnId = navBtn.getAttribute('id').split('-')[0]
    let sectionToDisplay = document.getElementById(navBtnId+'-section')
    hideSections()
    sectionToDisplay.style.display='block'
}

dashboardNavLinks.forEach(link=>link.addEventListener('click', ()=>{
    showSectionOnNavClick(link)
}))

// const fullProfileBtns =
//     Array.from(document.getElementsByClassName('full-profile-btn'))
//
// function getTrainee(ev){
//     return ev.target.getAttribute('id')
//
// }
// fullProfileBtns.forEach(btn=>btn.addEventListener('click', (ev)=>{
//     let trainee = getTrainee(ev)
//     document.getElementsByClassName('trainee-list')[0].style.display='none'
//     document.getElementsByClassName('trainee-details')[0].style.display='block'
// }))