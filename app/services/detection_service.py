import cv2 
from ultralytics import YOLO
import os

class DetectionService:
    def __init__(self):
        self.model = YOLO('yolov10n.pt')
    
    def detect_object(self, image_path):
        image = cv2.imread(image_path)
        results = self.model(image)

        detections = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = self.model.names[int(box.cls)]
                detections.append({
                    "x1": x1, "y1": y1, "x2": x2, "y2": y2, 
                    "confidence": conf, "class": cls
                })
        return {"detections": detections}

