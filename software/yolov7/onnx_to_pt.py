import torch
import onnx
from onnx2torch import convert

# path to onnx model
onnx_path = 'YoloV7-Tiny.onnx' # pretrained model from HaGRID

# path to save pt model to
pt_path = 'yolov7-tiny-HaGRID.pt'

# convert onnx to pytorch
onnx_model = onnx.load(onnx_path)
pytorch_model = convert(onnx_model)

# save pytorch model
torch.save(pytorch_model.state_dict(), pt_path)

print("Model saved successfully!")