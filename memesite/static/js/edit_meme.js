document.querySelectorAll("i");

let iEls = document.querySelectorAll("i");

for (let el of iEls) {
    el.addEventListener("click", (e) => console.log(e.target.dataset.id));
}

function deleteMeme(e){
    

}


function editMeme(meme_id){

}