
import customtkinter as ctk
from PIL import Image, ImageTk, ImageGrab
import threading
import time
import sys
from find_and_call import extract_text_from_clipboard_image
import tkinter as tk
from datetime import datetime

# Флаг и событие для работы скрипта
script_running = False
stop_event = threading.Event()

# Класс для перенаправления вывода в текстовое поле и файл с метками времени
class RedirectOutputToTextWidget:
    def __init__(self, text_widget, log_file_path):
        self.text_widget = text_widget
        self.log_file = open(log_file_path, 'a', encoding='utf-8')

    def write(self, message):
        if message.strip():  # Добавляем метку времени только если сообщение не пустое
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_message = f"[{timestamp}] {message}"
        else:
            formatted_message = message  # Для пустых строк просто добавляем перенос строки

        # Выводим в текстовое поле
        self.text_widget.insert(tk.END, formatted_message)
        self.text_widget.see(tk.END)  # Прокручиваем вниз при добавлении нового сообщения

        # Записываем в файл
        self.log_file.write(formatted_message)
        self.log_file.flush()

# Функция, которая запускает основной процесс в отдельном потоке
def run():
    global script_running
    print('Скрипт запущен')
    previous_image = None

    while script_running:
        # Проверяем буфер обмена на наличие изображения
        img = ImageGrab.grabclipboard()
        if isinstance(img, list):
            img = img[0]

        if img and img != previous_image:
            extract_text_from_clipboard_image()
            previous_image = img
        
        print('===========================================================')
        print(f"Состояние stop_event перед ожиданием: {stop_event.is_set()}")
        # Используем событие для уменьшения нагрузки на процессор
        stop_event.wait(1)
        print(f"Состояние script_running: {script_running}") 
        print(f"Состояние stop_event после ожидания: {stop_event.is_set()}")

# Функция для включения/выключения скрипта
def toggle_script():
    global script_running
    if switch_var.get() == 1:
        if not script_running:  # чтобы не запускать несколько потоков
            script_running = True
            stop_event.clear()  # Сбрасываем событие, чтобы запустить поток
            print("Автозвонок включен, script_running установлен в True, stop_event сброшен.")
            toggle_switch.configure(text="Автозвонок включен")
            # Запускаем run в отдельном потоке
            threading.Thread(target=run, daemon=True).start()
    else:
        script_running = False
        stop_event.set()  # Устанавливаем событие, чтобы остановить поток
        print("Автозвонок выключен, script_running установлен в False, stop_event установлен.")
        toggle_switch.configure(text="Автозвонок выключен")

# =================================================== #
#               Создаем интерфейс                     #
# =================================================== #

window = ctk.CTk(fg_color='#343535')
window.title('Auto Dialer')

# Добавляем иконку для окна
window.iconbitmap(r"Auto Dialer.ico")

window.geometry("550x888")  
window.resizable(True, True)

border_frame = ctk.CTkFrame(window, fg_color='#565656')
border_frame.pack(padx=5, pady=5, fill="both", expand=True)

CTkFrame = ctk.CTkFrame(border_frame, fg_color='#3D3D3D')
CTkFrame.pack(padx=10, pady=10, fill="both", expand=True)

switch_var = ctk.IntVar()  
toggle_switch = ctk.CTkSwitch(CTkFrame, text="Автозвонок выключен", variable=switch_var, command=toggle_script)
toggle_switch.place(relx=0.5, rely=0.3, anchor="s")

# Добавляем текстовое поле для отображения отладочной информации
debug_text = ctk.CTkTextbox(CTkFrame, width=500, height=500, fg_color='#1E1E1E', text_color='white', wrap="word")
debug_text.place(relx=0.5, rely=0.7, anchor="center")

# Перенаправляем вывод в текстовое поле и в файл
log_file_path = "debug_log.txt"
sys.stdout = RedirectOutputToTextWidget(debug_text, log_file_path)

window.mainloop()
