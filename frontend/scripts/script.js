document.body.onload = () => {
    fetch("http://127.0.0.1:5000/data/")
    .then((response) => {
        if (response.ok) {
            response.json()
            .then(data => {
                display_fetched_words(data.data)
            })
        } else {
            throw(new Error("Something went wrong"))
        }
    })
    .catch(error => {
        return error;
    })
}
function display_fetched_words(data){
   const list = document.querySelector(".words ul");
   data.forEach(element => {
    let li_element = document.createElement("li");
    li_element.innerText = element;
    list.appendChild(li_element);
   });
}