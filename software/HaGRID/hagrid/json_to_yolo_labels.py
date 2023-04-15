import json
import os

json_file = "annotations.json"
output_folder = "hand_labels"

with open(json_file, "r") as f:
    annotations = json.load(f)

for key, value in annotations.items():
    # Get the image filename
    image_filename = f"{key}.jpg"
    
    # Get the bounding box coordinates
    bboxes_coco = value["bboxes"]
    bboxes_yolo = []
    for bbox_coco in bboxes_coco:
        x, y, w, h = bbox_coco
        xc = x + w / 2
        yc = y + h / 2
        bboxes_yolo.append([xc, yc, w, h])
    
    # Get the labels and confidence score
    labels = value["labels"]
    conf_score = value["leading_conf"]
    
    # Save the YOLO label file
    label_filename = f"{key}.txt"
    label_path = os.path.join(output_folder, label_filename)
    with open(label_path, "w") as f:
        for bbox_yolo, label in zip(bboxes_yolo, labels):
            label_id = 0 # Assign a label ID (e.g., 0 for "hand")
            line = f"{label_id} {bbox_yolo[0]} {bbox_yolo[1]} {bbox_yolo[2]} {bbox_yolo[3]}"
            f.write(line + "\n")
