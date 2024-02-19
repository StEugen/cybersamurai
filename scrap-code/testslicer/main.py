from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

@app.route('/api/v1/upload/file', methods=['POST'])
def upload_html():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = file.filename
        file.save(os.path.join('./store/', filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})

@app.route('/api/v1/upload/json', methods=['POST'])
def upload_json():
    data = request.json
    if data and 'chapters' in data:
        chapters = data['chapters']
        with open('./store/data.json', 'w') as f:
            json.dump(data, f)

        # Search for chapters in uploaded file
        with open(os.path.join('./store/', 'index.html'), 'r') as file:
            file_contents = file.read()
            found_chapters = [chapter for chapter in chapters if chapter in file_contents]

        return jsonify({'message': 'JSON data uploaded successfully', 'found_chapters': found_chapters})
    else:
        return jsonify({'error': 'No JSON data provided or missing "chapters" key'})

if __name__ == '__main__':
    app.run(debug=True)


