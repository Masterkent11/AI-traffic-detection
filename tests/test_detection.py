import unittest
from app.services.detection_service import DetectionService
import os

class TestDetectionService(unittest.TestCase):
    def setUp(self):
        self.detection_service = DetectionService()
        self.image_path = "app/uploads/test_plate.jpeg"

    def test_detect_object(self):
        self.assertTrue(os.path.exists(self.image_path), "Test image does not exist!")
        results = self.detection_service.detect_object(self.image_path)
        self.assertIsInstance(results, dict, "Detection results should be a dictionary.")
        print("Test Passed! Detection Results:", results)

if __name__ == '__main__':
    unittest.main()
