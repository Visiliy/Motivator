const btn = document.querySelector('#btn');
const form_to_change = document.querySelector('#form_to_change');
let count = 0;

btn.onclick = function() {
    if (count % 2 == 0) {
        form_to_change.classList.remove('display_none');
        count++;
    }
    else {
        form_to_change.classList.add('display_none');
        count++;
    }
}