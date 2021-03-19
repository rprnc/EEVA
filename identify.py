import face_recognition
import cv2


# Peek Functionality - grabs a picture from the main camera - delete this picture later once the face recognition
def peek():
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    cap.release()
    return img


# # Lookup functionality - put this in a json file for lookups - move to redis if it gets huge - names and encodings basically

image_of_rob = face_recognition.load_image_file('./img/known/Rob Prince.jpg')
rob_face_encoding = face_recognition.face_encodings(image_of_rob)[0]

image_of_cerrie = face_recognition.load_image_file(
    './img/known/Cerrie Baines.jpg')
cerrie_face_encoding = face_recognition.face_encodings(image_of_cerrie)[0]

# Create array of encodings and names
known_face_encodings = [
    rob_face_encoding,
    cerrie_face_encoding
]

known_face_names = [
    "Rob",
    "Trouble"
]


# Identify Function

def identify(img):
    # Find faces in test image
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(
        img, face_locations)

    people = []
    name = "Unknown Person"

    # Loop through face_encodings in peek image and check for matches
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding)

        for i in matches:
            if i == True:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                people.append(name)

    return people
