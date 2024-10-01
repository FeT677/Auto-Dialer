import pytesseract
import pyperclip
import re
import webbrowser
from PIL import ImageGrab


#Задание пути к Тесеракту 
pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'


#Функция получения текста с картинки в буфере обмена
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
    

#Функция поиска номера на картинке
def find_phone_number(text):
    try:
        phone_number = re.findall(r'\+?\d[\d\s-]{7,}\d', text)
    except:
        print('Не найден номер телефона на изображении\n\n')

    if phone_number:
        formatted_phone_number = re.sub(r'[-\s]', '', phone_number[0])
        print(f"Найден номер телефона: {formatted_phone_number}")
        
        return formatted_phone_number
    else:
        print("Номер телефона не найден.")
        
        return None


#Функция отправки номера телефона в звонилку по протоколу TEL:
def open_softphone_and_call(phone_number):
    tel_url = f"tel:{phone_number}"
    # Открытие номера через протокол tel
    webbrowser.open(tel_url)