const { ipcRenderer } = require('electron');

const timer = document.getElementById('timer');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const hoursInput = document.getElementById('hours-input');
const minutesInput = document.getElementById('minutes-input');
const secondsInput = document.getElementById('seconds-input');

let timerInterval;
let countdownSeconds = 0;

function updateTimer() {
  countdownSeconds--;
  if (countdownSeconds < 0) {
    clearInterval(timerInterval);
    timer.innerHTML = '0:00:00';
  } else {
    const hours = Math.floor(countdownSeconds / 3600);
    const minutes = Math.floor((countdownSeconds % 3600) / 60);
    const seconds = countdownSeconds % 60;
    timer.innerHTML = `${hours}:${minutes < 10 ? "0" : ""}${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
  }
}

startButton.addEventListener('click', function() {
  const hours = parseInt(hoursInput.value);
  const minutes = parseInt(minutesInput.value);
  const seconds = parseInt(secondsInput.value);
  countdownSeconds = (hours * 3600) + (minutes * 60) + seconds;
  if (countdownSeconds > 0) {
    timerInterval = setInterval(updateTimer, 1000);
  }
});

stopButton.addEventListener('click', function() {
  clearInterval(timerInterval);
  countdownSeconds = 0;
  timer.innerHTML = '00:00:00';
});
        
