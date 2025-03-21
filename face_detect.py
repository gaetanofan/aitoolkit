from face_recognition.api import face_locations
from PIL import Image
import face_recognition
from IPython.display import display

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("_known/me.jpg")
face_locations = face_recognition.face_locations(image)

if (len(face_locations) > 1):
    print("Found {} faces .".format(len(face_locations)))
elif (len(face_locations) == 1):
    print("Found 1 faces.")
else:
    print("No faces.")

for face_location in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    display(pil_image) 
