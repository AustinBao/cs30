document.getElementById("add_meme").addEventListener("click", openModal);

// JavaScript for Modal
var modal = document.getElementById("memeModal");
var form = document.getElementById("memeForm");
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
function openModal() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
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
  var file = this.files[0]; // Get the selected file
  if (file) {
      var reader = new FileReader();

      reader.onload = function(e) {
          var imgElement = document.getElementById('imageDisplay');
          imgElement.src = e.target.result;
          imgElement.style.visibility = 'visible'; // Make the image visible
      };

      reader.readAsDataURL(file); // Convert the file into a data URL
  }
});

// Handle form submission
document.getElementById('memeForm').onsubmit = function(event) {
  event.preventDefault();

  // Get form values
  var description = document.getElementById('memeDescription').value;
  var time = document.getElementById('memeTime').value;
  var source = document.getElementById('memeSource').value;

  // Log the values to the console
  console.log("Description:", description);
  console.log("Time:", time);
  console.log("Source:", source);

  // Optionally, close the modal after processing
  modal.style.display = "none";
};




class Meme {
  constructor(name, description, time, source) {
      this.name = name;
      this.description = description;
      this.time = time;
      this.source = source;
  }

  display_info() {
      console.log(`Name: ${this.name}, Description: ${this.description}.`);
  }
}

const meme = new Meme("Ugandan Knuckles", "from sonic", "grade 5", "from elementary school friends");
meme.display_info();  
