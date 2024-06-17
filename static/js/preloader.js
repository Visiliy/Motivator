const btn_1 = document.querySelector('#btn_1');
const btn_2 = document.querySelector('#btn_2');
const preloader__wrapper = document.querySelector('#preloader__wrapper');
const control_div = document.querySelector('#control_div');
const text = document.querySelector('#text');
let timerID;

btn_2.onclick = function() {
    preloader__wrapper.classList.remove('display_none');
    control_div.classList.add('display_none');

    let counter = 0;

    timerID = setInterval(function(){
        if (counter == 0) {
            text.innerText = 'Выдох';
        }
        if (counter == 2) {
            text.innerText = 'Вдох';
        }
        if (counter == 5) {
            counter = -1;
        }
        counter += 1;
    }, 1000)
}
btn_1.onclick = function () {
    preloader__wrapper.classList.add('display_none');
    control_div.classList.remove('display_none');
    clearInterval(timerID);
    counter = 0;
}