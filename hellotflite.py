import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite

# Load the TensorFlow Lite model
#current file is yolo v5 which uses coco dataset (class id 2 = car)
interpreter = tflite.Interpreter(model_path='model/1.tflite')
interpreter.allocate_tensors()

# Prepare the image
image = Image.open('image/image.jpg')
image = image.resize((300, 300)).convert('RGB')
input_data = np.array(image, dtype=np.uint8)
input_data = np.expand_dims(input_data, axis=0)


# Set the input tensor
input_details = interpreter.get_input_details()
interpreter.set_tensor(input_details[0]['index'], input_data)

# Run the model
interpreter.invoke()

# Get the outputs
output_details = interpreter.get_output_details()
detection_boxes = interpreter.get_tensor(output_details[0]['index'])
detection_classes = interpreter.get_tensor(output_details[1]['index'])
detection_scores = interpreter.get_tensor(output_details[2]['index'])
num_detections = int(interpreter.get_tensor(output_details[3]['index'])[0])  # Number of detections

# Process the results
for i in range(num_detections):
    class_id = int(detection_classes[0][i])
    score = float(detection_scores[0][i])
    box = detection_boxes[0][i]
    if score > 0.5:  # Confidence threshold
        print(f"Detected class ID: {class_id} with confidence: {score}")
        print(f"Bounding Box: {box}")
