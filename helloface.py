import face_recognition
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the image path from environment variable
image_path = os.getenv('IMAGE_PATH')

# Lataa kuva
image = face_recognition.load_image_file(image_path)

# Etsi kasvot kuvasta
face_locations = face_recognition.face_locations(image)

# Tarkista, löytyikö kasvoja ja tulosta viesti
if face_locations:
    print("Kasvot löydetty!")
else:
    print("Ei löytynyt kasvoja.")
