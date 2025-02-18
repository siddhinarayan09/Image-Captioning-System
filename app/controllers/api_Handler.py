from flask import Blueprint,jsonify,request
from app.models.ObjectDetection import objectPredict
import os
api_handler = Blueprint("api_handler", __name__)

@api_handler.route("/loadModels", methods=["GET"])
def loadModels():
    try:
        pass
    except Exception as e:
        return e
    return jsonify("Models Loaded")

@api_handler.route("/uploadImage", methods=["POST"])
def upload_file():
    UPLOAD_FOLDER = "uploads"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    objectPredict(filepath)

    return jsonify({"message": "File uploaded successfully", "file_path": filepath})