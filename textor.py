# Import required packages
import cv2
import pytesseract
import os
cwd = os.getcwd()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("success.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

extext = pytesseract.image_to_string(img)
print(extext)
cv2.imshow('success',img)
cv2.waitKey(0)
