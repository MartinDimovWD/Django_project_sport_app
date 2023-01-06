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
