import face_recognition as fr
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Load known faces once when the app starts
known_face_encodings = []
known_face_names = []

def load_known_faces():
    # Load images from known_faces folder and encode
    kian_image = fr.load_image_file("known_faces/kian.jpg")
    kian_encoding = fr.face_encodings(kian_image)[0]
    known_face_encodings.append(kian_encoding)
    known_face_names.append("Kian")

    usain_image = fr.load_image_file("known_faces/usain bolt.jpg")
    usain_encoding = fr.face_encodings(usain_image)[0]
    known_face_encodings.append(usain_encoding)
    known_face_names.append("Usain Bolt")

    Elon_image = fr.load_image_file("known_faces/ellon musk.jpg")
    Elon_encoding = fr.face_encodings(Elon_image)[0]
    known_face_encodings.append(Elon_encoding)
    known_face_names.append("Elon Musk")

    # Add more known faces here:
    # e.g.
    # usain_image = fr.load_image_file("known_faces/usain_bolt.jpg")
    # usain_encoding = fr.face_encodings(usain_image)[0]
    # known_face_encodings.append(usain_encoding)
    # known_face_names.append("Usain Bolt")

load_known_faces()

@app.route('/recognize', methods=['POST'])
def recognize_face():
    file = request.files.get('image')
    if not file:
        return jsonify({"error": "No image received"}), 400

    # Read the uploaded image file into a numpy array
    img = fr.load_image_file(file)

    # Get face encodings in the uploaded image
    face_encodings = fr.face_encodings(img)

    if len(face_encodings) == 0:
        return jsonify({"error": "No face found in the image"}), 400

    face_encoding = face_encodings[0]

    # Compare face encoding to known faces
    matches = fr.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    return jsonify({"name": name})
