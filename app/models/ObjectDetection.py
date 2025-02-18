from ultralytics import YOLO
from flask import jsonify
import os 
def objectPredict(img_path):
    print("img_path")
    # Predict with the model
    model = YOLO("yolo11n.pt")  # load an official model
    results = model(img_path)  # predict on an image

    detected_objects = set()  # Use a set to store unique detected objects

    # Process results
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])  # Get the class ID of the detected object
            object_name = model.names[class_id]  # Convert class ID to object name
            detected_objects.add(object_name)  # Store detected objects

    print("Detected Objects in Image:", detected_objects)  # Print detected objects

    # # Process results list
    # for result in results:
    #     boxes = result.boxes  # Boxes object for bounding box outputs
    #     masks = result.masks  # Masks object for segmentation masks outputs
    #     keypoints = result.keypoints  # Keypoints object for pose outputs
    #     probs = result.probs  # Probs object for classification outputs
    #     obb = result.obb  # Oriented boxes object for OBB outputs
    #     print(boxes,masks,keypoints,probs,obb)
    #     result.save(filename=f"./outputs/YoloFormat_{img_path}.jpg")  # save to disk
        
    # Process results
    # return "Prediction complete!"  # No need to send JSON response to frontend