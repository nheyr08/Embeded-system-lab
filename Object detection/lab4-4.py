import cv2
import numpy as np

from ssd.classes import CLASSES_90

TRACKED_CLASSES = ["person", "bicycle", "car", "motorcycle"]
BOX_COLOR = (23, 230, 0)
TEXT_COLOR = (255, 255, 255)
INPUT_SIZE = (1920, 1080)


def illustrate_box(image: np.ndarray, box: np.ndarray, caption: str) -> None:
    rows, cols = image.shape[:2]
    points = box.reshape((2, 2)) * np.array([cols, rows])
    p1, p2 = points.astype(np.int32)
    cv2.rectangle(image, tuple(p1), tuple(p2), BOX_COLOR, thickness=4)
    cv2.putText(
        image,
        caption,
        tuple(p1),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        TEXT_COLOR,
        2)


def illustrate_detections(objects: np.ndarray, image: np.ndarray) -> np.ndarray:
    class_ids, scores, boxes = objects[:, 0], objects[:, 1], objects[:, 2:6]
    for class_id, score, box in zip(class_ids, scores, boxes):
        if CLASSES_90[int(class_id)] in TRACKED_CLASSES:
            illustrate_box(image, box, f"{CLASSES_90[int(class_id)]} {score:.2f}")
    return image


if __name__ == '__main__':
    # Read SSD model
    config = "ssd/ssd_mobilenet_v1_coco_2017_11_17.pbtxt.txt"
    model = "ssd/frozen_inference_graph.pb"
    detector = cv2.dnn.readNetFromTensorflow(model, config)

    # Read input image
    img = cv2.imread('images/street.png')

    # Initialize input
    detector.setInput(
        cv2.dnn.blobFromImage(
            img,
            size=INPUT_SIZE,
            swapRB=True,
            crop=False))

    # Do inference on image
    detections = detector.forward()[0, 0, :, 1:]
    scores = detections[:, 1]
    THRESHOLD = 0.3
    detections = detections[scores > THRESHOLD]

    # Draw result
    out = illustrate_detections(detections, img)

    cv2.imshow('lab4-4', img)

    cv2.waitKey()
    cv2.destroyAllWindows()
