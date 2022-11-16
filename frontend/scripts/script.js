document.body.onload = () => {
    fetch("http://127.0.0.1:5000/data/")
    .then((response) => {
        if (response.ok) {
            response.json()
            .then(data => {
                store_wordle_dataset(data.data);
            })
        } else {
            throw(new Error("Something went wrong"))
        }
    })
    .catch(error => {
        return error;
    })
}

function store_wordle_dataset(data){
    if(!localStorage.getItem('wordle_dataset')) {
        localStorage.setItem("wordle_dataset", JSON.stringify(data))
    }
}

function display_fetched_words(data){
   const list = document.querySelector(".words ul");
   data.forEach(element => {
    let li_element = document.createElement("li");
    li_element.innerText = element;
    list.appendChild(li_element);
   });
}

function submitGuess() {
    
}

function checkEnteredWord(inputElement) {
    const parrentWordInput = inputElement.parentElement;
    const userInputsArray = parrentWordInput.querySelectorAll('input');
    let userEnteredWord = "";
    userInputsArray.forEach(input => userEnteredWord += input.value);
    if (userEnteredWord.length == 5) {
        showGuessButton();
    } else {
        hideGuessButton();
    }
}

function showGuessButton() {
    document.querySelector("#userGuessButton").classList.remove('hidden');
}

function hideGuessButton() {
    document.querySelector("#userGuessButton").classList.add('hidden');
}

function getLastUserInput() {
    const userPlayground = document.querySelector('#userPlayground');
    const userInputs = document.querySelector('#userPlayground').querySelectorAll('.word-input');//array of user inputs [0, 1,2].len
    const lastUserInput = userInputs[userInputs.length - 1];
    return lastUserInput;
}