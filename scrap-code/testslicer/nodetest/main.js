const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const { JSDOM } = require('jsdom');
const path = require('path');

const app = express();
const port = 3000;

app.use(bodyParser.json());


app.post('/slice', (req, res) => {
    const { chapters } = req.body;
    const inputFile = 'input.html';
    const outputFolder = 'sliced_html_files';


    const outputFolderPath = path.join(__dirname, outputFolder);
    if (!fs.existsSync(outputFolderPath)) {
        fs.mkdirSync(outputFolderPath);
    }


    fs.readFile(inputFile, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading input file:', err);
            res.status(500).send('Internal Server Error');
            return;
        }

        const dom = new JSDOM(data);
        const document = dom.window.document;

        let slicing = false;
        let slicedContent = '';


        const traverse = node => {

            if (node.nodeType === 3 /* Node.TEXT_NODE */) {
                chapters.forEach(chapter => {
                    const chapterRegex = new RegExp(chapter.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i');
                    if (node.textContent.match(chapterRegex)) {
                        slicing = true;
                    }
                });
            }

            if (slicing) {
                slicedContent += node.outerHTML || node.textContent;
            }

            if (node.childNodes && node.childNodes.length) {
                for (let i = 0; i < node.childNodes.length; i++) {
                    traverse(node.childNodes[i]);
                }
            }

            if (node.tagName === 'H1' && chapters.includes(node.textContent.trim())) {
                slicing = false;
            }
        };
        traverse(document.body);

        const outputFileName = `${outputFolder}/sliced_output.html`;
        fs.writeFile(outputFileName, slicedContent, err => {
            if (err) {
                console.error('Error writing output file:', err);
                res.status(500).send('Internal Server Error');
                return;
            }
            console.log('HTML file sliced successfully:', outputFileName);
            res.status(200).send('HTML file sliced successfully');
        });
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
