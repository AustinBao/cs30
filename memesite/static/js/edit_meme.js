// "DOMContentLoaded" happens when the html page fully loads. Therefore prompting us to query the page for all icons.
document.addEventListener("DOMContentLoaded", function() {
    // list of all trash and edit icons on the home.html page
    let deleteIcons = document.querySelectorAll(".trash");
    let editIcons = document.querySelectorAll(".edit");
    
    // Looping through all "trash" icons and adding a click eventlistener that calls "deleteMeme" function
    for (let i = 0; i < deleteIcons.length; i++) {
        deleteIcons[i].addEventListener("click", function() { deleteMeme(this) });
    }
    // Looping through all "edit" icons and adding a click eventlistener that calls "editMeme" function
    for (let i = 0; i < editIcons.length; i++) {
        editIcons[i].addEventListener("click", function() { editMeme(this) });
    }
  });


function deleteMeme(iconElement) {
  // Find the meme card with the corresponding memeId
  let card = iconElement.closest(".card");
  let memeId = iconElement.dataset.id
  if (card) {
    fetch(`/delete_meme/${memeId}`, { method: 'DELETE', headers: {'Content-Type': 'application/json'} })
      .then(response => {
        if (response.ok) {
          console.log("Meme deleted");
          // Remove "card" from the html file
          card.remove();
        } else {
          console.error("Failed to delete meme");
        }
    }).catch(error => console.log(error))
  }
}


function editMeme(iconElement) {
  let card = iconElement.closest(".card2");
  let memeId = iconElement.dataset.id;
  let editmodal = document.getElementById("editMemeModal");
  let editspan = document.getElementById("editClose");

  if (card) {
    editmodal.style.display = "block";

    editspan.onclick = function() {
      editmodal.style.display = "none";
    };

    window.onclick = function(event) {
      if (event.target == editmodal) {
        editmodal.style.display = "none";
      }
    };

    document.getElementById('editImage').addEventListener('change', function() {
      let file = this.files[0];
      if (file) {
        let reader = new FileReader();

        reader.onload = function(e) {
          let imgElement = document.getElementById('editImageDisplay');
          imgElement.src = e.target.result;
          imgElement.hidden = false;
        };
        reader.readAsDataURL(file);
      }
    });

    let name = card.querySelector(".memeName");
    let description = card.querySelector(".memeDescription");
    let year = card.querySelector(".memeYear");
    let source = card.querySelector(".memeSource");

    let currentName = name.textContent;
    let currentDescription = description.textContent;
    let currentYear = year.textContent;
    let currentSource = source.textContent;

    document.getElementById('editName').value = currentName;
    document.getElementById('editDescription').value = currentDescription;
    document.getElementById('editYear').value = currentYear;
    document.getElementById('editSource').value = currentSource;

    document.getElementById('editMemeForm').onsubmit = function(event) {
      event.preventDefault();

      let form = event.target;
      let formData = new FormData(form);

      fetch(`/edit_meme/${memeId}`, { method: 'PUT', body: formData })
      .then(response => response.json())
      .then(data => {
        if (data) {
          editmodal.style.display = "none";
          console.log("Meme edited:", data);
          location.reload();
        } else {
          console.error("Failed to edit meme:", data);
        }
      })
      .catch(error => console.log(error))
    };
  }
}
