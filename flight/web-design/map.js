

var map_image_DOM_element = document.getElementById("map_image")
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

//

function generateGraphic() {
  console.log("generating flight!");

  const output_text = document.getElementById("output_text");

  //

  var first = [-118.408, 33.942]; //note:
  var seccond = [-6.27, 53.421]; //these are just examples
  //need to not have these hardcoded.

  output_text.innerHTML =
    "Congratulations! Your flight found is from LAX in Los Angeles to DUB in Dublin!";

  ctx.drawImage(map_image_DOM_element, 0, 0, canvas.width, canvas.height);
  ctx.beginPath();

  first = normalize(first);
  seccond = normalize(seccond);

  ctx.moveTo(first[0], first[1]);
  console.log(first, seccond);

  ctx.lineTo(seccond[0], seccond[1]);
  ctx.stroke();
}

function normalize(coord) {
  //[ [-180,180], [-90,90] ]
  coord[0] = ((coord[0] + 180) * 1000) / 360;
  coord[1] = 500 - ((coord[1] + 90) * 500) / 180;
  return coord;
}
