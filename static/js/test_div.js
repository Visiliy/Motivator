const btn_smiley_1 = document.querySelector('#click_1');
const btn_smiley_2 = document.querySelector('#click_2');
const btn_smiley_3 = document.querySelector('#click_3');
const btn_smiley_4 = document.querySelector('#click_4');
const btn_smiley_5 = document.querySelector('#click_5');
const btn_smiley_6 = document.querySelector('#click_6');
const btn_smiley_7 = document.querySelector('#click_7');

const test_div = document.querySelector('#test_div');
const span_form = document.querySelector('#span_form');
const card_form = document.querySelector('#card_form');
const error_div = document.querySelector('#error_div');

const test_question = document.querySelector('#test_question');
const label_1 = document.querySelector('#label_1');
const label_2 = document.querySelector('#label_2');
const label_3 = document.querySelector('#label_3');

const answer_1 = document.querySelector('#answer_1');
const answer_2 = document.querySelector('#answer_2');
const answer_3 = document.querySelector('#answer_3');
const btn_3 = document.querySelector('#btn_3');
const sicret_cod = document.querySelector('#sicret_cod');

const string_1 = 'Не волнуйтесь, Вы обязательно поправитесь! Главное - не падайте духом! Улыбнитесь, хорошее настроение помогает быстрее выздороветь!';
const string_2 = 'Мы рады, что у Вас прекрасное настороение! Желаем, чтобы оно оставалось как можно дольше!';
const string_3 = 'Как хорошо, что у Вас праздничное настроение! Отличное настроение продлевает жизнь, делает её яркой и незабываемой!';

const array_1 = ['Почему Вы плачете?', 'Всё идёт не так', 'Кто-то обижает', 'Чувствую моральную боль'];
const array_2 = ['Что вас огорчает?', 'Работа', 'Учёба', 'Жизнь'];
const array_3 = ['Почему Вы грустите?', 'Плохое настроение', 'Что-то не получается', 'Просто такое настроение'];
const array_4 = ['Почему у Вас состояние безразличия?', 'Потерян смысл жизни', 'Затяжная грусть', 'Не могу определиться по жизни'];

const object_1 = {1: ['Как часто у вас такое состояние?', 'Каждый день', 'Каждую неделю', 'Каждый месяц'], 2: ['Как скоро проходит это состояние?', 'Через день', 'Через неделю', 'Вообще не проходит!']};
const object_2 = {1: ['Как часто у вас такое состояние?', 'Каждый день', 'Каждую неделю', 'Каждый месяц'], 2: ['Что приводит вас к такому состоянию?', 'Неудачи', 'Всё идёт не по плану', 'Сам себе не нравлюсь']}
let default_object;
let count = 0;
let num;
let rate_value = [];
let click_namber;
let btn_ok;

if (hasCookie('permission') == false) {
    span_form.classList.remove('display_none');
};

const func = function(array, num_func, sicret_cod) {
    if (sicret_cod == 'no') {
        error_div.classList.remove('display_none');
    }
    else {
        span_form.classList.add('display_none');
        test_div.classList.remove('display_none');
        num = num_func;


        if (array[0] != undefined) {
            test_question.innerText = array[0];
        }

        if (array[1] != undefined) {
            label_1.innerText = array[1];
            answer_1.value = array[1];
        }

        if (array[2] != undefined) {
            label_2.innerText = array[2];
            answer_2.value = array[2];

        }

        if (array[3] != undefined) {
            label_3.innerText = array[3];
            answer_3.value = array[3];
        }
    }
}

const func_2 = function(string, sicret_cod) {
    if (sicret_cod == 'no') {
        error_div.classList.remove('display_none');
    }
    else {
        test_div.classList.add('display_none');
        card_form.classList.remove('display_none');

        const h2 = document.createElement('h2');
        const h4 = document.createElement('h4');
        const btn = document.createElement('button');

        h2.innerText = 'Пожелания';
        h2.classList.add('h2_form_div');

        h4.innerText = string;
        h4.classList.add('h2_form_div');
        h4.classList.add('margin_top');

        btn.innerText = 'Окей';
        btn.id = 'btn_ok';
        btn.classList.add('btn_result');

        card_form.append(h2);
        card_form.append(h4);
        card_form.append(btn);

        btn.onclick = function() {
            document.cookie = 'permission=1;max-age=60';
            window.location.href=`/mood/${click_namber}`;
        };
    }


}

btn_3.onclick = function() {
    if (document.querySelector('#answer_1').checked) {
        rate_value.push(document.querySelector('#answer_1').value);
    }
    if (document.querySelector('#answer_2').checked) {
        rate_value.push(document.querySelector('#answer_2').value);
    }
    if (document.querySelector('#answer_3').checked) {
        rate_value.push(document.querySelector('#answer_3').value);
    }
    answer_1.checked = false;
    answer_2.checked = false;
    answer_3.checked = false;
    count ++;
    if (count == num) {
        const result = document.querySelector('#result');
        test_div.classList.add('display_none');
        result.classList.remove('display_none');

        const h2 = document.createElement('h2');
        const btn = document.createElement('button');

        btn.innerText = 'Окей';
        btn.id = 'btn_ok';
        btn.classList.add('btn_result');


        h2.innerText = 'Пожелания';
        h2.classList.add('h2_form_div');

        result.append(h2);
        result.append(btn);

        btn.onclick = function() {
            document.cookie = 'permission=1;max-age=60';
            window.location.href=`/mood/${click_namber}`;
        };

    }
    else {
        const list = default_object[count];
        if (list[0] != undefined) {
            test_question.innerText = list[0];
        }

        if (list[1] != undefined) {
            label_1.innerText = list[1];
            answer_1.value = list[1];
        }

        if (list[2] != undefined) {
            label_2.innerText = list[2];
            answer_2.value = list[2];

        }

        if (list[3] != undefined) {
            label_3.innerText = list[3];
            answer_3.value = list[3];
        }
    }

};

btn_smiley_1.onclick = function() {
    func(array_1, 3, sicret_cod.innerHTML), default_object = object_1, click_namber = 1;
};
btn_smiley_2.onclick = function() {
    func(array_2, 3, sicret_cod.innerHTML), default_object = object_2, click_namber = 2;
};
btn_smiley_3.onclick = function() {
    func_2(string_1, sicret_cod.innerHTML), click_namber = 3;
};
btn_smiley_4.onclick = function() {
    func(array_3, 1, sicret_cod.innerHTML), default_object = 0, click_namber = 4;
};
btn_smiley_5.onclick = function() {
    func(array_4, 1, sicret_cod.innerHTML), default_object = 0, click_namber = 5;
};
btn_smiley_6.onclick = function() {
    func_2(string_2, sicret_cod.innerHTML), click_namber = 6;
};
btn_smiley_7.onclick = function() {
    func_2(string_3, sicret_cod.innerHTML), click_namber = 7;
};

function hasCookie(name) {
    return document.cookie.split(';').some(c => c.trim().startsWith(name + '='));
}