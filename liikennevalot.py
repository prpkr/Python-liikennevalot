#import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
from PIL import Image
import os
from dotenv import load_dotenv
import face_recognition

# Load environment variables
load_dotenv()

'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) #Green light
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) #yellow light
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) #red light
GPIO.setup(16, GPIO.IN) # PIR input
'''

'''
Code for Pir sensor
def sensor():
    print("Waiting for movement")
    while True:
        if GPIO.input(16):
            i = 1
        elif i == 1:
            sleep(0.1)
        else:
            print("Movement detected")
            break
'''

def setup_camera():
    """Setup the camera with the desired resolution."""
    camera = PiCamera()
    camera.resolution = (640, 480)
    return camera


def capture_image(camera, image_path):
    """Take a picture with the provided camera and save it."""
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
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
    """Detect faces in an image and return True if faces are found."""
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    if face_locations:
        print("Kasvot löydetty!")
        return True
    else:
        print("Ei löytynyt kasvoja.")
        return False

def greenlight():
    print("hello green")
    #GPIO.output(8, GPIO.HIGH)
    sleep(5)
    print("changing to red")
    #GPIO.output(8, GPIO.LOW)
    #GPIO.output(10, GPIO.HIGH)
    sleep(2)
    #GPIO.output(10, GPIO.LOW)

def redlight(camera, image_path):
    print("hello red")
    #GPIO.output(12, GPIO.HIGH)
    sleep(5)
    while True:  # Continuously capture images and detect faces
        capture_image(camera, image_path)
        if detect_faces(image_path):  # Check if faces were detected
            print("Face detected, changing to green")
            break  # Exit the loop if a face is detected
        else:
            print("No face detected, checking again")
            sleep(5)  # Wait a bit before the next check

    # Change to green light
    #GPIO.output(12, GPIO.LOW)
    #GPIO.output(10, GPIO.HIGH)
    sleep(2)
    #GPIO.output(10, GPIO.LOW)


def yellowlight():
    print("hello yellow")
    #GPIO.output(10, GPIO.HIGH)
    sleep(1)
    #GPIO.output(10, GPIO.LOW)
    sleep(1)

def main():
    image_path = os.getenv('IMAGE_PATH')
    camera = setup_camera()
    for i in range(3):
        yellowlight()
    while True:
        redlight(camera, image_path)
        greenlight()

if __name__ == "__main__":
    main()
