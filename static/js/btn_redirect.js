const btn = document.querySelector('#btn_redirect');
const a = document.querySelector('#href');

btn.onclick = function() {
    window.location.href='/entrance';
}

a.onclick = function() {
    const sicret_cod = document.querySelector('#sicret_cod');
    const entrance_2 = document.querySelector('#entrance_2');
    if (sicret_cod.innerHTML == 'no') {
        entrance_2.classList.remove('display_none');
    }
    else {
        window.location.href='/home';
    }
}