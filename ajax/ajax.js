let githubIdLink = "https://api.github.com/users/parth-gupta49";

let loader = document.querySelector(".loader");

let fetchBtn = document.getElementById("fetch-btn");

let elementToBePopulated = document.createElement('p');

let ourData =new XMLHttpRequest();
ourData.open('GET','https://learnwebcode.github.io/json-example/animals-1.json',true)

ourData.onload(()=>{
    console.log(ourData.responseText);
})












// fetchBtn.addEventListener("click", buttonClickHandler);

// function buttonClickHandler() {
//   console.log("clicked on button");
//   // instantiate an XHR object
//   const xhr = new XMLHttpRequest();
//   // Open the object
//   xhr.open("GET", "ajax.txt", true);

//   // what to do on progress
//   xhr.onprogress = function () {
//     console.log("On progress");
//     // Define the CSS for the loader
//     // const loaderCSS = `
//     // .loader {
//     //   border: 16px solid #f3f3f3;
//     //   border-radius: 50%;
//     //   border-top: 16px solid #3498db;
//     //   width: 120px;
//     //   height: 120px;
//     //   -webkit-animation: spin 2s linear infinite; /* Safari */
//     //   animation: spin 2s linear infinite;
//     // }

//     // /* Safari */
//     // @-webkit-keyframes spin {
//     //   0% { -webkit-transform: rotate(0deg); }
//     //   100% { -webkit-transform: rotate(360deg); }
//     // }

//     // @keyframes spin {
//     //   0% { transform: rotate(0deg); }
//     //   100% { transform: rotate(360deg); }
//     // }
//     // `;
//     // // Create a style element and set its content to the loaderCSS
//     // const styleElement = document.createElement('style');
//     // styleElement.textContent = loaderCSS;
//     // // Append the style element to the document head
//     // document.head.appendChild(styleElement);
//   };
//   // what to do when response is ready
//   xhr.onload = function () {
//     if (this.status === 200) {
//       console.log(this.responseText);
//     } else console.log("some error occurred");
//   };

//   xhr.send();
// }

// let counter = 0

// fetchBtn.addEventListener('click',populateData)

// function populateData() {
//     counter++;
//     if(counter<=3){
//         let ourRequest = new XMLHttpRequest();
//         ourRequest.open('GET',`https://learnwebcode.github.io/json-example/animals-${counter}.json`,true)
    
//         ourRequest.onload = function(){
//             let ourData = JSON.parse(ourRequest.responseText);
//             // let ourData = ourRequest.responseText;
//             // console.log(ourData);
    
//             renderHTML(ourData);
        
//         }
        
//         ourRequest.send();
//     }
//     else{
//         fetchBtn.disabled = true;
//     }
    
// }


// function renderHTML(data) {

//     let htmlString = "" ; 

//     for (let i = 0; i < data.length; i++) {
//         htmlString+="<p>" + data[i].name + "is a " + data[i].species + ".</p>"
//     }

//     elementToBePopulated.insertAdjacentHTML('beforeend',htmlString)
    



//     document.body.appendChild(elementToBePopulated)
// }








