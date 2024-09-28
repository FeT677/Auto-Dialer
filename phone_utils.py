import re
import webbrowser

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

def open_softphone_and_call(phone_number):
    tel_url = f"tel:{phone_number}"
    # Открытие номера через протокол tel
    webbrowser.open(tel_url)
