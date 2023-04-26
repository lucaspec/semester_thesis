import torch
from torchvision.models import mobilenet_v2
import onnx
import tf2onnx
import tensorflow as tf

# Load PyTorch model
pt_model = torch.load('yolov7-tiny.pt')
pt_model.eval()

sample_input = torch.rand((10, 2, 640, 640))

# Export PyTorch model to ONNX format
onnx_model_path = 'model.onnx'
torch.onnx.export(
    pt_model,               # PyTorch Model
    sample_input,           # Input tensor
    onnx_model_path,        # Output file 
    opset_version=12,       # Operator support version
    input_names=['input'],   # Input tensor name (arbitary)
    output_names=['output'] # Output tensor name (arbitary)
)

# Load the ONNX model
model = onnx.load("model.onnx")

# Check that the IR is well formed
onnx.checker.check_model(model)

# Print a Human readable representation of the graph
onnx.helper.printable_graph(model.graph)

# # Save ONNX model to a file
# onnx.save_model(onnx_model, 'model.onnx')

# # Load ONNX model
# onnx_model = onnx.load('model.onnx')

# # Convert ONNX model to TensorFlow Lite format
# tflite_model = convert.from_onnx(onnx_model)

# # Save TensorFlow Lite model to a file
# with open('model.tflite', 'wb') as f:
#     f.write(tflite_model)
