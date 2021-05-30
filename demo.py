import cv2
import pytesseract
import os
cwd = os.getcwd()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
vid = cv2.VideoCapture(0)

while(True):
	ret,frame = vid.read()
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv2.imshow('frame',frame)
cv2.imwrite(filename='saved.jpg',img = frame)
img = cv2.imread('saved.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
extext = pytesseract.image_to_string(img)
print(extext)
cv2.waitKey(0)
cv2.destroyAllWindows()