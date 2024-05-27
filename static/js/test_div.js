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
const btn_3 = document.querySelector('#btn_3');

const array_1 = ['Почему Вы плачете?', 'Всё идёт не так', 'Кто-то обижает', 'Чувствую моральную боль'];
const array_2 = ['Что вас огорчает?', 'Работа', 'Учёба', 'Жизнь'];

const object_1 = {1: ['Как часто у вас такое состояние?', 'Каждый день', 'Каждую неделю', 'Каждый месяц'], 2: ['Как скоро проходит это состояние?', 'Через день', 'Через неделю', 'Вообще не проходит!']};
const object_2 = {1: ['Как часто у вас такое состояние?', 'Каждый день', 'Каждую неделю', 'Каждый месяц'], 2: ['Что приводит вас к такому состоянию?', 'Неудачи', 'Всё идёт не по плану', 'Сам себе не нравлюсь']}
let default_object;
let count = 0;

const func = function(array) {
    test_div.classList.add('display_none');
    test_div.classList.remove('display_none');


    if (array[0] != undefined) {
        test_question.innerText = array[0];
    }

    if (array[1] != undefined) {
        label_1.innerText = array[1];
    }

    if (array[2] != undefined) {
        label_2.innerText = array[2];

    }

    if (array[3] != undefined) {
        label_3.innerText = array[3];
    }
}

btn_3.onclick = function() {
    count ++;
    const list = default_object[count];
    if (list[0] != undefined) {
        test_question.innerText = list[0];
    }

    if (list[1] != undefined) {
        label_1.innerText = list[1];
    }

    if (list[2] != undefined) {
        label_2.innerText = list[2];

    }

    if (list[3] != undefined) {
        label_3.innerText = list[3];
    }

};

btn_smiley_1.onclick = function() {
    func(array_1), default_object = object_1;
};
btn_smiley_2.onclick = function() {
    func(array_2), default_object = object_2;
};
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
