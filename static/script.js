function getWeather() {
  const city = document.getElementById("cityInput").value;

  fetch("/weather", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ city: city })
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      alert(data.error);
      return;
    }

    document.getElementById("locationName").textContent = data.location;
    document.getElementById("condition").textContent = `Condition: ${data.condition}`;
    document.getElementById("temperature").textContent = `Temperature: ${data.temperature} °C`;
    document.getElementById("humidity").textContent = `Humidity: ${data.humidity}%`;
    document.getElementById("wind").textContent = `Wind Speed: ${data.wind} kph`;
    document.getElementById("weatherIcon").src = data.icon;

    document.getElementById("weatherResult").classList.remove("hidden");
  })
  .catch(err => {
    console.error(err);
    alert("Something went wrong. Please try again.");
  });
}
