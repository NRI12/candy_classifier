import cv2
import torch
from PIL import Image
from torchvision.transforms import functional as F
from yolov5.models.experimental import attempt_load
from yolov5.utils.general import non_max_suppression, scale_coords
from yolov5.utils.plots import Annotator
from yolov5.utils.torch_utils import select_device

def predict_from_camera(weights=r'C:\Users\pc\Desktop\alll_x\runs\train\exp5\weights\best.pt', conf_thres=0.5, iou_thres=0.45):
    # Load model
    device = select_device('')
    model = attempt_load(weights, map_location=device)
    stride = int(model.stride.max())

    # Set model to evaluation mode
    model.eval()

    # Capture video from camera
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame from BGR to RGB
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert to PIL Image
        img = Image.fromarray(img)

        # Resize and pad image to fit model input shape
        img = F.resize(img, (640, 640))
        img = F.pad(img, (0, 0, (640 - img.size[1]) // 2, (640 - img.size[0]) // 2), fill=0)

        # Convert PIL Image to tensor
        img = F.to_tensor(img).float().unsqueeze(0).to(device)

        # Perform inference
        with torch.no_grad():
            pred = model(img)[0]

        # Post-process predictions
        pred = non_max_suppression(pred, conf_thres, iou_thres)[0]

        # Annotate image with bounding boxes and class labels
        annotator = Annotator(frame, line_width=3, text_size=2)
        if pred is not None:
            pred[:, :4] = scale_coords(img.shape[2:], pred[:, :4], frame.shape).round()
            for det in pred:
                annotator.box_label(det[:4], f'Class {int(det[5])}')
        annotated_frame = annotator.result()

        # Display annotated frame
        cv2.imshow('YOLOv5 Object Detection', annotated_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    predict_from_camera()
