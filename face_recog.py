import face_recognition

# Load the jpg files into numpy arrays
known_image = face_recognition.load_image_file("_known/me1.jpg")
lena_image = face_recognition.load_image_file("_known/lena.png")
unknown_image = face_recognition.load_image_file("_unknown/me2.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, 
# it returns a list of encodings. For the sake of 
# simplicity, we only consider the first encoding 
# in each image, so we grab index 0.

try:
    known_face_encoding = face_recognition.face_encodings(known_image)[0]
    lena_face_encoding = face_recognition.face_encodings(lena_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces. Check the image files. Aborting...")
    quit()

known_faces = [
    known_face_encoding,
    lena_face_encoding
]

known_names = [
    "Gaetano",
    "Lena"
] 

# results is an array of True/False telling if the 
# unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

if results[0] == True:
    print("It's a picture of " + (known_names)[0])
elif results[1] == True:
    print("It's a picture of " + (known_names)[1])
else:
    print("Don't know")   
