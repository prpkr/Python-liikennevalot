from picamera import PiCamera
from time import sleep
from PIL import Image
import os
from dotenv import load_dotenv
import face_recognition

# Load environment variables
load_dotenv()

def setup_camera():
    """Set up the camera and take a picture, saving it to the specified path."""
    image_path = os.getenv('IMAGE_PATH')
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    camera = PiCamera()
    try:
        camera.start_preview()
        sleep(2)  # Camera warm-up time
        camera.capture(image_path)
    finally:
        camera.stop_preview()
    return image_path

def display_image(image_path):
    """Display the image using PIL."""
    img = Image.open(image_path)
    img.show()

def detect_faces(image_path):
    """Detect faces in an image and print a message about detection."""
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    if face_locations:
        print("Kasvot löydetty!")
    else:
        print("Ei löytynyt kasvoja.")

def main():
    image_path = setup_camera()
    display_image(image_path)
    detect_faces(image_path)

if __name__ == "__main__":
    main()
