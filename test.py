import pyautogui
import pyttsx3
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Users\Avikdeb\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = Image.open("speech.png")
output = pytesseract.image_to_string(img)

speech = pyttsx3.init()
speech.say(output)
speech.runAndWait()
