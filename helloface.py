import face_recognition

# Lataa kuva
image = face_recognition.load_image_file("your_image.jpg")

# Etsi kasvot kuvasta
face_locations = face_recognition.face_locations(image)

# Tarkista, löytyikö kasvoja ja tulosta viesti
if face_locations:
    print("Kasvot löydetty!")
else:
    print("Ei löytynyt kasvoja.")
