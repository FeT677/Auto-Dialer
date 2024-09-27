import time
from find_and_call import extract_text_from_clipboard_image
from PIL import ImageGrab

class ScriptRunner:
    def run(self):
        print('Скрипт запущен\n\n')

        while True:
            if self.wait_for_png_in_clipboard():
                extract_text_from_clipboard_image()
            time.sleep(1)

    def wait_for_png_in_clipboard(self):
        print("Ожидание PNG в буфере обмена...")

        while True:
            img = ImageGrab.grabclipboard()
            if isinstance(img, list) and img:
                img = img[0]
            if img and img.format == 'PNG':
                print("PNG найден в буфере обмена.")
                return True
            time.sleep(1)


if __name__ == "__main__":
    runner = ScriptRunner()
    runner.run()
    