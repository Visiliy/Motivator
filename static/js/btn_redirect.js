const btn = document.querySelector('#btn_redirect');
const a = document.querySelector('#href');
const sicret_cod = document.querySelector('#sicret_cod');
const entrance_2 = document.querySelector('#entrance_2');

btn.onclick = function() {
    window.location.href='/entrance';
}

a.onclick = function() {
    if (sicret_cod.innerHTML == 'no') {
        entrance_2.classList.remove('display_none');
    }
    else {
        window.location.href='/home';
    }
}