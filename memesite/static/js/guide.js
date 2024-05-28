document.getElementById("guide").addEventListener("click", openModal);

let guidemodal = document.getElementById("guideModal");
let guidespan = document.getElementById("guideClose");

function openModal() {
  guidemodal.style.display = "block";
}

// when clicking the "x"
guidespan.onclick = function() {
  guidemodal.style.display = "none";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == guidemodal) {
    guidemodal.style.display = "none";
  }
}



