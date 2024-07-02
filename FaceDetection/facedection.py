

import cv2
# from google.colab.patches import cv2_imshow

#  pre-trained Haar cascade classifier from OpenCV
haar_cascade_path = './haarcascade_frontalface_default.xml'


face_cascade = cv2.CascadeClassifier(haar_cascade_path)

# Load the image
image_path = './group.jpg'  # Change to your image path
image = cv2.imread(image_path)

image = cv2.imread(image_path)

# Check if the image was loaded correctly
if image is None:
    print(f"Error: Unable to load image at path {image_path}")
else:
    # Convert the image to grayscale for channel 1
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Check if any faces are detected
    if len(faces) == 0:
        print("No faces detected.")
    else:
        print(f"Detected {len(faces)} faces.")
        # Draw bounding boxes around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 255), 2)
           
            
        # Display the output image with detected faces
        cv2.imshow("face",image)
        cv2.waitKey(0)

    
cv2.destroyAllWindows()