from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recognize', methods=['POST'])
def recognize_face():
    file = request.files.get('image')
    if file:
        print("Got image:", file.filename)
        # Future: Add face recognition here
        return jsonify({"name": "Kian"})  # Dummy name for now
    return jsonify({"error": "No image received"}), 400
