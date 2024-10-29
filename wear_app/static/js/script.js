const nav = document.querySelector(".nav__menu");
const burger = document.querySelector(".burger")

burger.addEventListener('click', function(){
    burger.classList.toggle('active');
    nav.classList.toggle('active');
})

