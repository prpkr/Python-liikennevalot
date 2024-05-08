from picamera import PiCamera
from time import sleep
from PIL import Image
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the image path from environment variable
image_path = os.getenv('IMAGE_PATH')

# Ensure the directory exists
os.makedirs(os.path.dirname(image_path), exist_ok=True)

# Set up the camera
camera = PiCamera()

try:
    # Start the camera preview
    camera.start_preview()
    sleep(2)  # Camera warm-up time
    camera.capture(image_path)
finally:
    # Stop the preview regardless of any errors during capture
    camera.stop_preview()

# Display the image using PIL
img = Image.open(image_path)
img.show()
