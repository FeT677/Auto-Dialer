import customtkinter as ctk
from PIL import ImageGrab
import threading
from find_and_call import extract_text_from_clipboard_image
import time


script_running = False
stop_event = threading.Event()


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
            toggle_switch.configure(text="Распознование ВКЛЮЧЕНО")
            threading.Thread(target=run, daemon=True).start()
    else:
        script_running = False
        stop_event.set()
        toggle_switch.configure(text="Распознование ВЫКЛЮЧЕНО")


##### Создаем интерфейс #####


window = ctk.CTk(fg_color="#343535")
window.title("Auto Dialer")

window.iconbitmap(r"Auto Dialer.ico")

window.geometry("275x100")
window.resizable(False, False)

border_frame = ctk.CTkFrame(window, fg_color="#565656")
border_frame.pack(padx=5, pady=5, fill="both", expand=True)

CTkFrame = ctk.CTkFrame(border_frame, fg_color="#3D3D3D")
CTkFrame.pack(padx=10, pady=10, fill="both", expand=True)

switch_var = ctk.IntVar()
toggle_switch = ctk.CTkSwitch(
    CTkFrame, text="Распознование ВЫКЛЮЧЕНО", variable=switch_var, command=toggle_script
)
toggle_switch.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()
