import tensorflow as tf

# Provide the paths for your input .pb model and output .tflite model
pb_model_path = './'
tflite_model_path = 'best-server.tflite'

def convert_pb_to_tflite(pb_model_path, tflite_model_path):
    # Load the saved model in .pb format
    loaded_model = tf.saved_model.load(pb_model_path)
    
    # Convert the model to TensorFlow Lite format
    converter = tf.lite.TFLiteConverter.from_saved_model(pb_model_path)
    tflite_model = converter.convert()

    # Save the converted model to .tflite file
    with open(tflite_model_path, 'wb') as f:
        f.write(tflite_model)

    print("Conversion completed successfully.")


# Call the conversion function
convert_pb_to_tflite(pb_model_path, tflite_model_path)