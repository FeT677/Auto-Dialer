import customtkinter as ctk
from PIL import ImageGrab, Image
import threading
from find_and_call import extract_text_from_clipboard_image
import time
import pystray
from pystray import MenuItem as item
import sys


script_running = False
stop_event = threading.Event()
window_hidden = False


# Запуск
def run():
    global script_running
    previous_image = None
    previous_copy_time = 0

    while script_running:
        img = ImageGrab.grabclipboard()
        if isinstance(img, list):
            img = img[0]
        if img:
            current_time = time.time()
            if img != previous_image or (
                img == previous_image and current_time - previous_copy_time > 1
            ):
                extract_text_from_clipboard_image()
                previous_image = img
                previous_copy_time = current_time
        stop_event.wait(1)


# Функция для включения/выключения скрипта
def toggle_script():
    global script_running
    if switch_var.get() == 1:
        if not script_running:
            script_running = True
            stop_event.clear()
            toggle_switch.configure(text="Автозвонок включён")
            threading.Thread(target=run, daemon=True).start()
    else:
        script_running = False
        stop_event.set()
        toggle_switch.configure(text="Автозвонок выключен")


def hide_window():
    global window_hidden
    window.withdraw()
    window_hidden = True
    create_tray_icon()


def show_window(icon, item):
    global window_hidden
    icon.stop()  # Остановить иконку трея
    window.deiconify()  # Восстановить окно
    window_hidden = False


def quit_window(icon, item):
    icon.stop()
    window.quit()
    sys.exit()


def create_tray_icon():
    image = Image.open("Auto Dialer.ico")
    
    menu = (item('Развернуть', show_window), item('Выход', quit_window))
    icon = pystray.Icon("Auto Dialer", image, "Auto Dialer", menu)
    icon.run()


##### Создаем интерфейс #####

window = ctk.CTk(fg_color="#343535")
window.title("Auto Dialer")

window.iconbitmap(r"Auto Dialer.ico")

window.geometry("275x150")
window.resizable(False, False)

border_frame = ctk.CTkFrame(window, fg_color="#565656")
border_frame.pack(padx=5, pady=5, fill="both", expand=True)

CTkFrame = ctk.CTkFrame(border_frame, fg_color="#3D3D3D")
CTkFrame.pack(padx=10, pady=10, fill="both", expand=True)

switch_var = ctk.IntVar()
toggle_switch = ctk.CTkSwitch(
    CTkFrame, text="Автозвонок выключен", variable=switch_var, command=toggle_script
)
toggle_switch.place(relx=0.5, rely=0.3, anchor="center")  # Центрируем по горизонтали, изменяем rely для позиционирования по вертикали

minimize_button = ctk.CTkButton(CTkFrame, text="Спрятать окно (свернуть в трей)", command=hide_window)
minimize_button.place(relx=0.5, rely=0.7, anchor="center")  # Центрируем кнопку по горизонтали, ниже по вертикали

window.mainloop()
