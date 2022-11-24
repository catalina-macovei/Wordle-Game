document.body.onload = () => {
    isEntropy = false;
    if (localStorage.getItem('isEntropy')) {
        isEntropy = JSON.parse(localStorage.getItem('isEntropy'));
    }
    handleEntropySwitcher(isEntropy);
    fetch("http://127.0.0.1:5000/data/?isEntropy=" + (isEntropy ? "1" : "0"))
    .then((response) => {
        if (response.ok) {
            response.json()
            .then(data => {
                store_wordle_dataset(data.data);
                if (isEntropy) {
                    localStorage.setItem('entropySet', JSON.stringify(data.entropy_set));
                    showEntropySuggestions()
                }
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
    isEntropy = false;
    if (localStorage.getItem('isEntropy')) {
        isEntropy = JSON.parse(localStorage.getItem('isEntropy'));
    }

    if (isInDataset(userWord)) {
        fetch("http://127.0.0.1:5000/user/?input=" + userWord + '&isEntropy=' + (isEntropy ? "1" : "0"))
        .then((response) => {
            if (response.ok) {
                response.json()
                .then(data => {                    
                    if (isEntropy) {
                        localStorage.setItem('entropySet', JSON.stringify(data.entropy_set));
                        showEntropySuggestions()

                    }
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
}


function showEntropySuggestions() {
    const entropyContainer = document.querySelector('#entropySuggestionsContainer');
    entropyContainer.innerHTML = `<h3 class="text-center my-1">Suggestions list:</h3>    `
    if (localStorage.getItem('entropySet')) {
        const entropySet = JSON.parse(localStorage.getItem('entropySet')) ?? [];
        entropySet.forEach((word, index) => {
            let newSuggestion = document.createElement('p');
            newSuggestion.innerText = `${index + 1}. ${word}`;
            entropyContainer.append(newSuggestion);
        })
    }
    
    entropyContainer.classList.remove('hidden');
}