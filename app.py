from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/find', methods=['POST'])
def find_file_size():
    # 1. Ensure the request has a file attached
    if 'image' not in request.files:
        return jsonify({"error": "No file provided. Please send a file with the key 'image'."}), 400
    
    file = request.files['image']
    
    # 2. Ensure the file isn't empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # 3. Calculate file size safely without loading it all into memory
    file.seek(0, 2)  # Move to the end of the file
    file_size_bytes = file.tell()  # Get the current position (size in bytes)
    file.seek(0)  # Reset the cursor back to the beginning

    return jsonify({
        "message": "File received successfully",
        "filename": file.filename,
        "file_size_bytes": file_size_bytes
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)