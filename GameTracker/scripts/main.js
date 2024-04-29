let cityInput = document.getElementById("city");
let leftdisplay = document.getElementById("mainDisplayLeft");
let middisplay = document.getElementById("mainDisplayMid");
let rightdisplay = document.getElementById("mainDisplayRight");
let time = document.getElementById("times");
let select = document.getElementById("favcities");
let star = document.getElementById("favstar");
let weatherImg = document.getElementById("weatherIcon");

document.getElementById("submitbtn").addEventListener("click", getWeatherData);

function resetPage() {
  leftdisplay.innerHTML = "";
  middisplay.innerHTML = "";
  rightdisplay.innerHTML = "";
  time.innerHTML = "";
  star.style.visibility = "hidden";
  document.getElementById("rain").innerHTML = "";
  document.getElementById("snow").innerHTML = "";
  weatherImg.src = "backgrounds/weatherapi.png";
}

async function getWeatherData() {
  // Get users city
  let city = cityInput.value;
  let apiKey = "063bdab6bd3f0e17b1afe04736c947ff";

  // Calling Api and return in form of JSON file
  let response = await fetch(
    `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=en&pop=metric&rain=metric&clouds=metric`
  );

  if (response.status === 400) {
    document.getElementById("result").innerHTML = "Please Enter A City";
    resetPage();
    throw new Error("No City to Search");
  } else if (response.status === 404) {
    document.getElementById("result").innerHTML = "City Not Found";
    resetPage();
    throw new Error("No City Found");
  } else {
    resetPage();
    star.style.visibility = "visible";
  }
  // waits for response then parses data as a JSON for later use
  let data = await response.json();
  dislpayWeatherData(data);
}
