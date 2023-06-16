var map_image_DOM_element = document.getElementById("map_image")
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

function generateGraphic() {
  console.log("generating flight!");

  // Fetch flight data from the /get_flight/ API
  fetch('/get_flight/')
    .then(response => response.json())
    .then(data => {
      // Handle the JSON data received from the server
      console.log(data);

      const output_text = document.getElementById("output_text");

      // Extract the flight information from the data object
      const departureAirport = data.departure.airport;
      const arrivalAirport = data.arrival.airport;

      output_text.innerHTML = `Congratulations! Your flight is from ${departureAirport} to ${arrivalAirport}!`;

      ctx.drawImage(map_image_DOM_element, 0, 0, canvas.width, canvas.height);
      ctx.beginPath();

      // Extract the coordinates from the flight data or use your hardcoded values
      // TODO: DATA.ARRIVAL.IATA OR DATA.DEPARTURE.IATA GETS THE DATA!
      var first = [data.departure.longitude, data.departure.latitude];
      var second = [data.arrival.longitude, data.arrival.latitude];

      first = normalize(first);
      second = normalize(second);

      ctx.moveTo(first[0], first[1]);
      console.log(first, second);

      ctx.lineTo(second[0], second[1]);
      ctx.stroke();
    })
    .catch(error => {
      console.error('Error:', error);
      // Handle any errors that occur during the request
    });
}

function normalize(coord) {
  //[ [-180,180], [-90,90] ]
  coord[0] = ((coord[0] + 180) * 1000) / 360;
  coord[1] = 500 - ((coord[1] + 90) * 500) / 180;
  return coord;
}