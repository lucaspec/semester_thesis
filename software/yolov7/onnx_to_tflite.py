from onnx_tf.backend import prepare
import onnx
import tensorflow as tf

# Convert from onnx to TF
onnx_model_path = 'yolov7-tiny.onnx'
tf_model_path = 'model_tf'

onnx_model = onnx.load(onnx_model_path)
tf_rep = prepare(onnx_model)
tf_rep.export_graph(tf_model_path)


# Convert from TF to TF Lite
saved_model_dir = 'model_tf'
tflite_model_path = 'model.tflite'

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)