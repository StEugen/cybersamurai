const { ipcRenderer } = require('electron');

ipcRenderer.on('timer-start', () => {
  console.log('Timer started');
});

ipcRenderer.on('timer-stop', () => {
  console.log('Timer stopped');
});


let startTime;
let timerInterval;
let duration;

function startTimer() {
  ipcRenderer.send('timer-start');
  duration = parseInt(document.getElementById('hours').value) * 3600 +
             parseInt(document.getElementById('minutes').value) * 60 +
             parseInt(document.getElementById('seconds').value);
  if (duration > 0) {
    document.getElementById('startButton').disabled = true;
    document.getElementById('stopButton').disabled = false;
    startTime = process.hrtime();
    timerInterval = setInterval(updateTimer, 1);
  }
}

function updateTimer() {
  const currentTime = process.hrtime(startTime);
  const elapsedSeconds = (currentTime[0] * 1000 + currentTime[1] / 1000000) / 1000;
  const remainingSeconds = Math.max(duration - elapsedSeconds, 0);
  const hours = Math.floor(remainingSeconds / 3600);
  const minutes = Math.floor((remainingSeconds % 3600) / 60);
  const seconds = Math.floor(remainingSeconds % 60);
  const milliseconds = Math.round((remainingSeconds % 1) * 1000);
  const elapsed = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}.${milliseconds.toString().padStart(3, '0')}`;
  document.getElementById('timer').innerHTML = elapsed;
  if (remainingSeconds <= 0) {
    stopTimer();
  }
}

function stopTimer() {
    ipcRenderer.send('timer-stop');
    clearInterval(timerInterval);
    document.getElementById('startButton').disabled = false;
    document.getElementById('stopButton').disabled = true;
    document.getElementById('timer').innerHTML = '00:00:00.000';
  }
  
