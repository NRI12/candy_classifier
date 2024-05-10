import torch
import cv2
from PIL import Image
import numpy as np
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load YOLOv5 model
model = torch.hub.load('.', 'custom', path=r'C:\Users\pc\Desktop\alll_x\runs\train\exp5\weights\best.pt', source='local')

# Video
video_path = r'C:\Users\pc\Desktop\alll_x\5.mp4'
prev_classes = set()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Unable to open video")
    exit()

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(frame_rgb)

    results = model(pil_image)
   # Get unique class labels in the current frame
    unique_classes = set(results.xyxy[0][:, -1].int().tolist())

    new_classes = unique_classes - prev_classes

    # Print unique class labels when they change
    for cls in new_classes:
        print(f'Unique class: {model.names[int(cls)]}')
    prev_classes = unique_classes

    # Draw bounding boxes on the frame
    for *box, conf, cls in results.xyxy[0].tolist():
            box = [int(i) for i in box]
            if conf > 0.6:  
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 255), 3) 
                cv2.putText(frame, f'{model.names[int(cls)]} {conf:.2f}', (box[0], box[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)  

    # Display the resulting frame
    cv2.imshow('YOLOv5 Object Detection', frame)
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
cap.release()
cv2.destroyAllWindows()
