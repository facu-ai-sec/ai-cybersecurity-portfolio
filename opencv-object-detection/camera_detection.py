import cv2
import numpy as np

net = cv2.dnn.readNetFromCaffe(
    "scripts/MobileNetSSD_deploy.prototxt",
    "scripts/MobileNetSSD_deploy.caffemodel"
)

CLASSES = {
    0: "background",
    1: "aeroplane",
    2: "bicycle",
    3: "bird",
    4: "boat",
    5: "bottle",
    6: "bus",
    7: "car",
    8: "cat",
    9: "chair",
    10: "cow",
    11: "diningtable",
    12: "dog",
    13: "horse",
    14: "motorbike",
    15: "person",
    16: "pottedplant",
    17: "sheep",
    18: "sofa",
    19: "train",
    20: "tvmonitor"
}

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No camera was detected")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not read the frame")
        break

    (h, w) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        frame,
        scalefactor=0.007843,
        size=(300, 300),
        mean=127.5
    )

    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            x1, y1, x2, y2 = box.astype("int")

            label = CLASSES[class_id]
            text = f"{label}: {confidence:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2
            )

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
