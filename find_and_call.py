import pytesseract
from PIL import ImageGrab
import pyperclip
import logging
import time
from phone_utils import find_phone_number, open_softphone_and_call

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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

def on_button_click():
    from image_handler import wait_for_new_image_in_clipboard  # Используем функцию из image_handler
    previous_image = None
    img = wait_for_new_image_in_clipboard(previous_image)
    if img:
        print("PNG найден в буфере обмена.")
        logging.info("PNG найден в буфере обмена.")
        previous_image = img
        extracted_text = extract_text_from_clipboard_image()
        if extracted_text:
            phone_number = find_phone_number(extracted_text)
            if phone_number:
                open_softphone_and_call(phone_number)
        else:
            print("Текст не найден на изображении.")
