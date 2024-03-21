let githubIdLink = "https://api.github.com/users/parth-gupta49";

let loader = document.querySelector(".loader");

let fetchBtn = document.getElementById("fetch-btn");

let elementToBePopulated = document.createElement('p');



fetchBtn.addEventListener('click', clickButton)

function clickButton() {
    let ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json',false)

    // ourRequest.onload = () => {
    //     // console.log(ourData.responseText);

    //     let ourData = JSON.parse(ourRequest.responseText)
    //     console.log(ourData[0]);

    // }

    ourRequest.onload = function(){
        if(this.status === 200)
            console.log(this.responseText);
    }

    ourRequest.send()
    console.log("this works just fine");
}


