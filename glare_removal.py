

# # Removing glare
# import cv2

# # Load the image
# img = cv2.imread('/home/plato/Downloads/receipt2.jpeg')

# # Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply a Gaussian blur
# blur = cv2.GaussianBlur(gray, (5, 5), 0)

# # Threshold the image
# _, thresh = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY)

# # Apply an inpainting algorithm
# dst = cv2.inpaint(img, thresh, 3, cv2.INPAINT_TELEA)

# # Display the result
# cv2.imshow('Original image', img)
# cv2.imshow('Processed image', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Adaptive thresholding
import cv2
import pytesseract
import os


# Load the image
img = cv2.imread('/home/plato/Downloads/receipt2.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
preprocessed_img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 3)

# # Display the result
# cv2.imshow('Original image', img)
# cv2.imshow('Processed image', thresh)
os.chdir('/home/plato/Pictures')
# Filename
filename = 'Preprocessed_receipt1.jpg'
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, preprocessed_img)
  
# List files and directories  
# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'  
  
print('Successfully saved')# cv2.waitKey(0)
# cv2.destroyAllWindows()

