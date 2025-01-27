import cv2

# Load the pre-trained face detection model (Haar Cascade Classifier) for detecting faces.
face_cascade = cv2.CascadeClassifier(
    "c:/Users/acer/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
)

# Initialize video capture from the default webcam (ID 0).
video_capture = cv2.VideoCapture(0)

while True:  # Infinite loop to continuously capture video frames
    # Read a single frame from the webcam.
    # `ret` is a boolean indicating success, and `video_data` is the frame data.
    ret, video_data = video_capture.read()

    # Convert the frame to grayscale for better performance in face detection.
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame using the Haar Cascade Classifier.
    # `scaleFactor`: Specifies the image scaling (1.1 means reduce by 10% each iteration).
    # `minNeighbors`: Number of neighbors a rectangle must have to be considered a face.
    # `minSize`: Minimum size of detected faces (30x30 pixels).
    faces = face_cascade.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )

    # Loop through all detected faces and draw rectangles around them.
    for (x, y, w, h) in faces:
        # Draw a green rectangle around the detected face.
        # (x, y) is the top-left corner, and (x+w, y+h) is the bottom-right corner.
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the video frame with rectangles around detected faces.
    cv2.imshow("Video_Live", video_data)

    # Break the loop if the 'a' key is pressed.
    if cv2.waitKey(10) == ord("a"):
        break

# Release the webcam resource after exiting the loop.
video_capture.release()

# Close all OpenCV windows that were opened.
cv2.destroyAllWindows()
