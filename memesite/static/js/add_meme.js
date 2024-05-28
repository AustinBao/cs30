document.getElementById("add_meme").addEventListener("click", openModal);

let addmodal = document.getElementById("memeModal");
let addform = document.getElementById("addMemeForm");
let addspan = document.getElementById("addClose");

function openModal() {
  addmodal.style.display = "block";
}

// when clicking the "x"
addspan.onclick = function() {
  addmodal.style.display = "none";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == addmodal) {
    addmodal.style.display = "none";
  }
}


// Updates the img when adding a meme
document.getElementById('memeImage').addEventListener('change', function() {
  let file = this.files[0]; // Get the selected file
  if (file) {
    let reader = new FileReader();

      reader.onload = function(e) {
        let imgElement = document.getElementById('imageDisplay');
          imgElement.src = e.target.result;
          imgElement.hidden = false; 
      };
      reader.readAsDataURL(file); // Convert the file into a data URL
  }
});


