import cv2

def detect_blindness(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply an adaptive threshold to segment the image
    _, threshold = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contours were found
    if len(contours) > 0:
        print("Blindness detected!")
    else:
        print("No blindness detected.")

# Path to the image you want to test
image_path = "C:\Users\itsan\OneDrive\Desktop\Hand-Written-Digit-Recognition-master\Hand-Written-Digit-Recognition-master\b.jpg"

# Call the function to detect blindness
detect_blindness(image_path)
