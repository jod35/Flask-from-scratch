const form = document.querySelector('form');
const x = document.querySelector('#x');
const y = document.querySelector('#y');
const result = document.querySelector('.result');
const clear_button = document.querySelector('#clear');




const URL = '/add'



form.addEventListener('submit', (e) => {

    console.log(x.value);
    console.log(y.value);

    let x_value = parseInt(x.value)
    let y_value = parseInt(y.value)

    let request_options = {
        method: "POST",
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify({ x: x_value, y: y_value })
    }

    fetch(URL, request_options)
        .then(response => response.json())
        .then((data) => {
            form.reset();
            result.innerHTML += `<p>${x_value} + ${y_value}= ${data.result}</p>`
        })
        .catch((err) => console.log(err))

    e.preventDefault();
})


clear_button.addEventListener('click', () => {
    result.innerHTML = ""
})