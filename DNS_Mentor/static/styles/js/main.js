const openPopUp = document.getElementById('open_pop_up');
const openPopUpBurger = document.getElementById('open_pop_up_burger');
const closePopUp = document.getElementById('pop_up_close');
const popUp = document.getElementById('pop_up');

openPopUp.addEventListener('click', function(e){
    e.preventDefault();
    popUp.classList.add('active');
})

openPopUpBurger.addEventListener('click', function(e){
  e.preventDefault();
  popUp.classList.add('active');
})

closePopUp.addEventListener('click', () =>{
    popUp.classList.remove('active');
})

const openPopUpA = document.getElementById('open_pop_up_a');
const closePopUpA = document.getElementById('pop_up_close_a');
const popUpA = document.getElementById('pop_up_a');

openPopUpA.addEventListener('click', function(e){
    e.preventDefault();
    popUpA.classList.add('active');
})


closePopUpA.addEventListener('click', () =>{
    popUpA.classList.remove('active');
})