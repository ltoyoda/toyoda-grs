//File part of irock

// after loading the page, when  you click the button it calls the function handleButtonClick
window.onload = init;
function init() {
    var button = document.getElementById("addButton");  // addButton = id created in the irock file
    button.onclick = handleButtonClick;
    loadPlaylist();                                     // ul id = playlist - Displays playlist when load the page
}

function handleButtonClick() {
//    alert("Button was clicked!");                   // to check if the function is working
    var textInput = document.getElementById("songTextInput"); // the element we want to get from the DOM
    var songName = textInput.value;  // to get the text which was typed into the input field
    var li = document.createElement("li");  // creating a new (free floating) element - li = kind of element
    li.innerHTML = songName;  // sets the contents of <li> to the song name
    var ul = document.getElementById("playlist"); // find the ul element
    ul.appendChild(li); //  adds the <li> element to the <ul> element, as a child and after the contents of the list
    save(songName); // save the names each time time it is added
}


