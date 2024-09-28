import os
import time
import pytesseract
import pyperclip
from PIL import ImageGrab

from phone_utils import find_phone_number, open_softphone_and_call

current_dir = os.path.dirname(os.path.abspath(__file__))
pytesseract.pytesseract.tesseract_cmd = os.path.join(current_dir, 'Tesseract-OCR', 'tesseract.exe')

def wait_for_new_image_in_clipboard(previous_image=None):
    while True:
        img = ImageGrab.grabclipboard()
        if isinstance(img, list):
            img = img[0]

        if img != previous_image:
            return img
        time.sleep(1)

def extract_text_from_clipboard_image():
    img = ImageGrab.grabclipboard()

    if isinstance(img, list):
        img = img[0]

    if isinstance(img, ImageGrab.Image.Image):
        extracted_text = pytesseract.image_to_string(img)

        if extracted_text.strip():
            print(f"Распознанный текст: {extracted_text}")
            pyperclip.copy(extracted_text)
            print("Текст скопирован в буфер обмена.")
            if find_phone_number(extracted_text):
                open_softphone_and_call(extracted_text)
        else:
            print("Текст не найден на изображении.\n\n")
            pyperclip.copy('')
            return None
    else:
        print("Изображение не найдено в буфере обмена.")
        pyperclip.copy('')
        return None
