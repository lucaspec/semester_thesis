import torch

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5n")  # or yolov5n - yolov5x6, custom
model.cpu() # or .cuda()

# Images
img = "city-streets.png"  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.save()  # or .show(), .save(), .crop(), .pandas(), etc.