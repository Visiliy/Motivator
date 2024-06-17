const btn_1 = document.querySelector('#btn_1');
const btn_2 = document.querySelector('#btn_2');
const preloader__wrapper = document.querySelector('#preloader__wrapper');
const control_div = document.querySelector('#control_div');

btn_2.onclick = function() {
    preloader__wrapper.classList.remove('display_none');
    control_div.classList.add('display_none');
}
btn_1.onclick = function () {
    preloader__wrapper.classList.add('display_none');
    control_div.classList.remove('display_none');
}