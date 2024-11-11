import pytesseract
import pyperclip
import re
import webbrowser
from PIL import ImageGrab


# Задание пути к Тесеракту
pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

# Функция получения текста с картинки в буфере обмена
def extract_text_from_clipboard_image():
    img = ImageGrab.grabclipboard()
    if isinstance(img, list):
        img = img[0]
    if isinstance(img, ImageGrab.Image.Image):
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789-'
        extracted_text = pytesseract.image_to_string(img, config=custom_config)
        if extracted_text.strip():
            pyperclip.copy(extracted_text)
            if find_phone_number(extracted_text):
                print(f'Полученный номер {extracted_text}')
                open_softphone_and_call(extracted_text)
        else:
            pyperclip.copy("")
            return None
    else:
        pyperclip.copy("")
        return None


# Функция отбора номера телефона в распознанном тексте
def find_phone_number(text):
    try:
        phone_number = re.findall(r"\+?\d[\d\s-]{7,}\d", text)
    except:
        pass
    if phone_number:
        formatted_phone_number = re.sub(r"[-\s]", "", phone_number[0])
        return formatted_phone_number
    else:
        return None


# Функция отправки номера телефона в звонилку по протоколу TEL:
def open_softphone_and_call(phone_number):
    tel_url = f"tel:{phone_number}"
    webbrowser.open(tel_url)
