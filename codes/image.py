import cv2

# Read an image
img = cv2.imread("C:/Users/adith/OneDrive/Desktop/Internship 6.0 social media post template.png")   # replace with your file path

# Check if image loaded successfully
if img is None:
    print("Error: Could not read image.")
else:
    # Show the image in a window
    cv2.imshow("My Image", img)

    # Wait until a key is pressed, then close
    cv2.waitKey(0)
    cv2.destroyAllWindows()