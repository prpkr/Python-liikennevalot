from picamera import PiCamera
from time import sleep
from PIL import Image

# Set up the camera
camera = PiCamera()

# Capture the image
camera.start_preview()
sleep(5)  # Camera warm-up time
camera.capture('/home/pi/image.jpg')
camera.stop_preview()

# Display the image
img = Image.open('/home/pi/image.jpg')
img.show()
