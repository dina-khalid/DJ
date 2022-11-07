


playBtn = document.getElementById("play");
stopBtn = document.getElementById("stop");
volumeBtn = document.getElementById("volume");
var wavesurfer = WaveSurfer.create({
  container: "#waveform",
  waveColor: "#e3bbee",
  progressColor: "#fe38ab",
  barHeight: 4,
  reponsive: true,
  hideScrollbar: true
});
var wavesurfer1 = WaveSurfer.create({
  container: "#waveform1",
  waveColor: "#e3bbee",
  progressColor: "#fe38ab",
  barHeight: 4,
  reponsive: true,
  hideScrollbar: true
});
wavesurfer1.load("static/audio/guitar.wav");
wavesurfer.load("static/audio/guitar.wav");

playBtn.onclick = function () {
  wavesurfer.playPause();
  wavesurfer1.playPause();
  if (playBtn.src.match("play")) playBtn.src = "static/images/pause.png";
  else playBtn.src = "static/images/play.png";
};
stopBtn.onclick = function () {
  wavesurfer.stop();
  wavesurfer1.stop();
  playBtn.src = "static/images/play.png";
};

volumeBtn.onclick = function () {
  wavesurfer.toggleMute();
  wavesurfer1.toggleMute();
  if (volumeBtn.src.match("volume"))
    volumeBtn.src = "static/images/mute.png";
  else volumeBtn.src = "static/images/volume.png";
};
var slider = document.querySelector("#slider");

slider.oninput = function () {
  var zoomLevel = Number(slider.value);
  wavesurfer.zoom(zoomLevel);
  wavesurfer1.zoom(zoomLevel);
};

// let waves = document.getElementById('waveform').children
// console.log(waves)
// for(let i=0;i<waves.length;i++){
// }







/*scroll buttons */
let values =  JSON.parse(document.getElementById("flask_data").getAttribute("data"));
console.log(values)
let n = Object.keys(values).length;
let str = ""
for (let i =0 ; i<n;i++){
    str += 
    `<div class="container">
        <div class="number" id="number${i}">${values[`slider${i}`]["value"]}</div>
        <input type="range" min="-10" max="10" value=${values[`slider${i}`]["value"]} class="slider" id="slider${i}" name="slider${i}">

        <div style = "transform: rotate(90deg);">${values[`slider${i}`]["name"]}</div>
    </div>`

}

str +=     
`<input type = "file" name = "file" style="margin:10px"/>
<input type = "submit"/>` 
document.getElementsByClassName("all-sliders")[0].innerHTML = str

const sliders = document.getElementsByClassName("slider")
const number = document.getElementsByClassName("number")
for (let i = 0 ;i<=number.length;i++){
  sliders[i].oninput = function(){
      number[i].innerHTML = sliders[i].value 
  }
}