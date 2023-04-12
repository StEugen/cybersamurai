const { ipcRenderer } = require('electron');
const { join } = require('path');

function uploadFile() {
    fetch('dump.json')
        .then(response => response.blob())
        .then(blob => {
            const file = new File([blob], 'dump.json');
            const dt = new DataTransfer();
            dt.items.add(file);
            input.files = dt.files;

            input.dispatchEvent(new Event('change'));

            const absPath = join(__dirname, 'dump.json');

            ipcRenderer.send('file-uploaded', absPath);
        });
}

uploadFile();
