const btn_smiley_1 = document.querySelector('#click_1');
const btn_smiley_2 = document.querySelector('#click_2');
const btn_smiley_3 = document.querySelector('#click_3');
const btn_smiley_4 = document.querySelector('#click_4');
const btn_smiley_5 = document.querySelector('#click_5');
const btn_smiley_6 = document.querySelector('#click_6');
const btn_smiley_7 = document.querySelector('#click_7');
const test_div = document.querySelector('#test_div');
const span_form = document.querySelector('#span_form');

const func_1 = function() {
    test_div.classList.add('display_none');
    test_div.classList.remove('display_none');

}
const func_2 = function() {
    span_form.classList.add('display_none');
    test_div.classList.remove('display_none');

}
const func_3 = function() {
    span_form.classList.add('display_none');
    test_div.classList.remove('display_none');

}
const func_4 = function() {
    span_form.classList.add('display_none');
    test_div.classList.remove('display_none');

}
const func_5 = function() {
    span_form.classList.add('display_none');
    test_div.classList.remove('display_none');

}
const func_6 = function() {
    span_form.classList.add('display_none');
    test_div.classList.remove('display_none');

}
const func_7 = function() {
    span_form.classList.add('display_none');
    test_div.classList.remove('display_none');

}

btn_smiley_1.addEventListener('click', func_1);
btn_smiley_2.addEventListener('click', func_2);
btn_smiley_3.addEventListener('click', func_3);
btn_smiley_4.addEventListener('click', func_4);
btn_smiley_5.addEventListener('click', func_5);
btn_smiley_6.addEventListener('click', func_6);
btn_smiley_7.addEventListener('click', func_7);