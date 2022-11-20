document.body.onload = () => {
    isEntropy = false;
    if (localStorage.getItem('isEntropy')) {
        isEntropy = JSON.parse(localStorage.getItem('isEntropy'));
    }
    handleEntropySwitcher(isEntropy);
    fetch("http://127.0.0.1:5000/data/?isEntropy=" + isEntropy)
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

function submitGuess() {
    const userWord = getUserWord(getLastUserInput());
    if (isInDataset(userWord)) {
        fetch("http://127.0.0.1:5000/user/?input=" + userWord)
        .then((response) => {
            if (response.ok) {
                response.json()
                .then(data => {
                    console.log(data);
                    disableInputs();
                    if (data.isGuessed) {
                        wordIsGuessed();
                    } else {
                        if (data.correctIndexes.length) {
                            data.correctIndexes.forEach(index => markIndex('green', index))
                        }
                        if (data.existingIndexes.length) {
                            data.existingIndexes.forEach(index => markIndex('yellow', index))
                        }
                        addNewInputRow();
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
    displayCongratulationsMessage();
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

function disableInputs() {
    getUserInputRow().querySelectorAll('input').forEach(input => input.disabled = true);
}

function getUserInputRow() {
    const userInputs = document.querySelector('#userPlayground').querySelectorAll('.word-input');//array of user inputs [0, 1,2].len
    const lastUserInputs = userInputs[userInputs.length - 1];
    return lastUserInputs;
}

function addNewInputRow() {
    const userPlayGround = document.querySelector('#userPlayground');
    const userInputsContainerDiv = document.createElement('div');
    userInputsContainerDiv.classList.add('flex', 'justify-center', 'gap-2', 'word-input');
    for(let i = 0; i < 5; i++) {
        userInputsContainerDiv.append(generateInput())
    }
    userPlayGround.append(userInputsContainerDiv);
}

function generateInput() {
    const input = document.createElement('input');
    input.type = 'text'; 
    input.maxLength = 1;
    input.oninput = () => checkEnteredWord(input);
    input.pattern = "[A-Z]";
    input.classList.add('w-12', 'rounded-md', 'text-center');
    return input;
}

function displayCongratulationsMessage() {
    const pyroDiv = document.querySelector('.pyro');
    const innerDiv= document.createElement('div');
    innerDiv.classList = 'before';
    pyroDiv.append(innerDiv);
    innerDiv.classList.remove('before');
    innerDiv.classList.add('after');
    pyroDiv.append(innerDiv);
    showResetButton();
}

function showResetButton() {
    const resetBtn = document.querySelector('#userGuessButton');
    resetBtn.innerText = 'Start new game';
    resetBtn.classList.remove('hidden');
    resetBtn.onclick = () => location.reload();
}

function toggleEntropy(element) {
    const input = element.querySelector('input');
    localStorage.setItem('isEntropy', JSON.stringify(input.checked));
    location.reload();
}

function handleEntropySwitcher(isEntropy) {
    const entropySwitcher = document.querySelector('#entropySwitcher');
    entropySwitcher.querySelector('span').innerText = isEntropy ? "entropy on" : "no entropy";
    entropySwitcher.querySelector('input').checked = isEntropy;
    if (isEntropy) {
        showEntropySuggestions()
    }
}


function showEntropySuggestions() {
    document.querySelector('#entropySuggestionsContainer').classList.remove('hidden');
}