const btn_smiley_1 = document.querySelector('#click_1');
const btn_smiley_2 = document.querySelector('#click_2');
const btn_smiley_3 = document.querySelector('#click_3');
const btn_smiley_4 = document.querySelector('#click_4');
const btn_smiley_5 = document.querySelector('#click_5');
const btn_smiley_6 = document.querySelector('#click_6');
const btn_smiley_7 = document.querySelector('#click_7');

const test_div = document.querySelector('#test_div');
const span_form = document.querySelector('#span_form');

const test_question = document.querySelector('#test_question');
const label_1 = document.querySelector('#label_1');
const label_2 = document.querySelector('#label_2');
const label_3 = document.querySelector('#label_3');

const answer_1 = document.querySelector('#answer_1');
const answer_2 = document.querySelector('#answer_1');
const answer_3 = document.querySelector('#answer_3');

const array_1 = ['Почему Вы плачете?', 'Всё идёт не так', 'Кто-то обижает', 'Чувствую моральную боль'];

const func = function(array) {
    test_div.classList.add('display_none');
    test_div.classList.remove('display_none');

    const p_1 = document.createElement('p');
    const p_2 = document.createElement('p');
    const p_3 = document.createElement('p');
    const p_4 = document.createElement('p');

    if (array[0] != undefined) {
        p_1.innerText = array[0];
    }

    if (array[1] != undefined) {
        p_2.innerText = array[1];
    }

    if (array[2] != undefined) {
    p_3.innerText = array[2];

    }

    if (array[3] != undefined) {
        p_4.innerText = array[3];
    }

    test_question.append(p_1);
    label_1.append(p_2);
    label_2.append(p_3);
    label_3.append(p_4);
}

btn_smiley_1.addEventListener('click', function() {
    func(array_1);
});
btn_smiley_2.addEventListener('click', function() {
    func(2);
});
btn_smiley_3.addEventListener('click', function() {
    func(3);
});
btn_smiley_1.addEventListener('click', function() {
    func(1);
});
btn_smiley_4.addEventListener('click', function() {
    func(4);
});
btn_smiley_5.addEventListener('click', function() {
    func(5);
});
btn_smiley_6.addEventListener('click', function() {
    func(6);
});
btn_smiley_7.addEventListener('click', function() {
    func(7);
});
