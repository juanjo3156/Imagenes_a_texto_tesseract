import cv2
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


#insertando imagen 
imagen = cv2.imread('chiste.png')
imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(imagen))
cv2.imshow('Result',imagen)
cv2.waitKey(0)

# insertamos la segunda imagen 
imagen2 = cv2.imread('telefono.png')
imagen2 = cv2.cvtColor(imagen2,cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(imagen2))
cv2.imshow('Result',imagen2)
cv2.waitKey(0)