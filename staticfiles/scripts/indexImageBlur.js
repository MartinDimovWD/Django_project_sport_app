const indexBackgroundImage = document.getElementById('index-background-image');
const traineeSignUpItem = document.getElementById('trainee-sign-up-item');
const coachSignUpItem = document.getElementById('coach-sign-up-item');


coachSignUpItem.addEventListener('mouseover', ()=>{
    indexBackgroundImage.src='static/images/sign-up/coach-focus.jpg';
})
coachSignUpItem.addEventListener('mouseout', ()=>{
    indexBackgroundImage.src='static/images/sign-up/coach-n-trainer-index-img.png';
})
traineeSignUpItem.addEventListener('mouseover', ()=>{
    indexBackgroundImage.src='static/images/sign-up/trainee-focus.jpg';
})
traineeSignUpItem.addEventListener('mouseout', ()=>{
    indexBackgroundImage.src='static/images/sign-up/coach-n-trainer-index-img.png';
})

