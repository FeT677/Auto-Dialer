import customtkinter as ctk
from PIL import Image, ImageTk, ImageGrab
import threading
from find_and_call import extract_text_from_clipboard_image
import time

# Флаг и событие для работы скрипта
script_running = False
stop_event = threading.Event()

# Функция, которая запускает основной процесс в отдельном потоке
def run():
    global script_running
    print('Скрипт запущен\n\n')
    previous_image = None

    previous_image = None
    previous_copy_time = 0  # Время последнего копирования изображения

    while script_running:
        # Проверяем буфер обмена на наличие изображения
        img = ImageGrab.grabclipboard()
        if isinstance(img, list):
            img = img[0]

        if img:
            current_time = time.time()  # Текущее время
            if img != previous_image or (img == previous_image and current_time - previous_copy_time > 1):
                extract_text_from_clipboard_image()
                previous_image = img
                previous_copy_time = current_time  # Обновляем время последнего копирования

        # Используем событие для уменьшения нагрузки на процессор
        stop_event.wait(1)

# Функция для включения/выключения скрипта
def toggle_script():
    global script_running
    if switch_var.get() == 1:
        if not script_running:  # чтобы не запускать несколько потоков
            script_running = True
            stop_event.clear()  # Сбрасываем событие, чтобы запустить поток
            print("Автозвонок включен")
            toggle_switch.configure(text="Автозвонок включен")
            # Запускаем run в отдельном потоке
            threading.Thread(target=run, daemon=True).start()
    else:
        script_running = False
        stop_event.set()  # Устанавливаем событие, чтобы остановить поток
        print("Автозвонок выключен")
        toggle_switch.configure(text="Автозвонок выключен")

# =================================================== #
#               Создаем интерфейс                     #
# =================================================== #

window = ctk.CTk(fg_color='#343535')
window.title('Auto Dialer')

# Добавляем иконку для окна
window.iconbitmap(r"Auto Dialer.ico")

window.geometry("250x100")  
window.resizable(False, False)

border_frame = ctk.CTkFrame(window, fg_color='#565656')
border_frame.pack(padx=5, pady=5, fill="both", expand=True)

CTkFrame = ctk.CTkFrame(border_frame, fg_color='#3D3D3D')
CTkFrame.pack(padx=10, pady=10, fill="both", expand=True)

switch_var = ctk.IntVar()  
toggle_switch = ctk.CTkSwitch(CTkFrame, text="Автозвонок выключен", variable=switch_var, command=toggle_script)
toggle_switch.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()
