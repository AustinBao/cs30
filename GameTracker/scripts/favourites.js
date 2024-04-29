// testing
let favouritesString = localStorage.getItem("favourites");
let favourites;
if (favouritesString) {
  favourites = favouritesString.split(",");
} else {
  favourites = [];
}
console.log(favourites);

for (let i = 0; i < favourites.length; i++) {
  let city = document.createElement("option");
  city.value = favourites[i];
  city.innerHTML =
    favourites[i].charAt(0).toUpperCase() + favourites[i].slice(1);
  select.appendChild(city);
}

document
  .getElementById("favcities")
  .addEventListener("click", function (event) {
    cityInput.value = event.target.value;
    star.style.color = "orange";
  });

function addFavourite(city) {
  let citytag = document.createElement("option");
  citytag.value = city;
  citytag.innerHTML = city;
  select.appendChild(citytag);
  star.style.color = "orange";
}

function removeFavourite(index) {
  select.remove(index);
  star.style.color = "grey";
}

star.addEventListener("click", function () {
  let city = cityInput.value.toLowerCase();
  let index = favourites.indexOf(city);

  // index returns -1 if the city is not in the favourites list. Also updates select tag every time a new city is removed or added
  if (index === -1) {
    addFavourite(city);
    favourites.push(city);
  } else {
    removeFavourite(index);
    favourites.splice(index, 1);
  }
  console.log(favourites);
  localStorage.setItem("favourites", favourites);
});
