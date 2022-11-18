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
    const userWord = getUserWord(getLastUserInput());
    if (isInDataset(userWord)) {
        fetch("http://127.0.0.1:5000/user/?input=" + userWord)
        .then((response) => {
            if (response.ok) {
                response.json()
                .then(data => {
                    console.log(data);
                    if (data.isGuessed) {
                        wordIsGuessed();
                    } else {
                        if (data.correctIndexes.length) {
                            data.correctIndexes.forEach(index => markIndex('green', index))
                        }
                        if (data.existingIndexes.length) {
                            data.existingIndexes.forEach(index => markIndex('yellow', index))
                        }
                    }
                })
            } else {
                throw(new Error("Something went wrong"))
            }
        })
        .catch(error => {
            return error;
        })
    } else {
        displayError("Your word isn't valid:(((");
    }
}

function isInDataset(word){
    const dataset = JSON.parse(localStorage.getItem("wordle_dataset"));
    return dataset.indexOf(word) > -1;
}
function displayError(message){
    const userError = document.querySelector(".userError");
    userError.classList = 'text-xs userError mb-4 text-red-500';
    userError.innerText = message;
}

function getUserWord(inputElement){
    const parrentWordInput = inputElement.parentElement;
    const userInputsArray = parrentWordInput.querySelectorAll('input');
    let userEnteredWord = "";
    userInputsArray.forEach(input => userEnteredWord += input.value);
    return userEnteredWord.toUpperCase();
}

function checkEnteredWord(inputElement) {
    let userEnteredWord = getUserWord(inputElement);
    if (userEnteredWord.length == 5 && isAlpha(userEnteredWord)) {
        showGuessButton();
    } else {
        hideGuessButton();
    }
}

function isAlpha(word){
    let isAlpha = true;
    [...word].forEach(character => {
        if (character < "A" || character > "Z"){
            isAlpha = false;
        }
    })
    return isAlpha;
}


function showGuessButton() {
    document.querySelector("#userGuessButton").classList.remove('hidden');
}

function hideGuessButton() {
    document.querySelector("#userGuessButton").classList.add('hidden');
}

function getLastUserInput() {
    const lastUserInput = getUserInputRow().querySelector('input');
    return lastUserInput;
}

function wordIsGuessed() {
    const arr = Array.from(Array(5).keys())
    arr.forEach(index => markIndex("green", index));
}
/*
function letterIsGuessed(){
    const arr = Array.from(Array(5).keys())
    arr.forEach(index => markIndex("yellow", index));
}
*/
function markIndex(color, index) {
    const userInputs = getUserInputRow().querySelectorAll('input');
    userInputs[index].classList.add("bg-" + color + "-500");
}

function getUserInputRow() {
    const userPlayground = document.querySelector('#userPlayground');
    const userInputs = document.querySelector('#userPlayground').querySelectorAll('.word-input');//array of user inputs [0, 1,2].len
    const lastUserInputs = userInputs[userInputs.length - 1];
    return lastUserInputs;
}