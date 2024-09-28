
from find_and_call import extract_text_from_clipboard_image, wait_for_new_image_in_clipboard

def run():
    print('Скрипт запущен\n\n')

    while True:
        if wait_for_new_image_in_clipboard():
            extract_text_from_clipboard_image()

if __name__ == "__main__":
    run()
    