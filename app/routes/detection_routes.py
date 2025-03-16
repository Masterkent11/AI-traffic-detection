from flask import Blueprint, request, jsonify
from app.services.detection_service import DetectionService

detection_bp = Blueprint("detection", __name__)

detection_service = DetectionService()


@detection_bp.route('/detect', methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({'error': 'No image uploader'}, 400)
    
    file = request.files["image"]
    filepath = save_uploaded_file(file)

    if not filepath:
        return jsonify({'error': 'No image uploader'}, 400)
    
    
