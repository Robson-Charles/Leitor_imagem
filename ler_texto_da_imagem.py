import os

import pytesseract
import cv2




def iniciar():

    image = cv2.imread("Captcha.jpg")

    pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR\\tesseract.exe"

    texto = pytesseract.image_to_string(image)
    try:

        os.remove('Captcha.txt')
    except:
        print('')
    #os.remove('Captcha.jpg')
    return texto

#iniciar()
