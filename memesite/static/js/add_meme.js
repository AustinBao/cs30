document.getElementById("add_meme").addEventListener("click", openModal);

let modal = document.getElementById("memeModal");
let form = document.getElementById("addMemeForm");
let span = document.getElementById("addClose");

function openModal() {
  modal.style.display = "block";
}

// when clicking the "x"
span.onclick = function() {
  modal.style.display = "none";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


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