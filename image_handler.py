import time
from PIL import ImageGrab

def wait_for_new_image_in_clipboard(previous_image):
    while True:
        img = ImageGrab.grabclipboard()
        if isinstance(img, list):
            img = img[0]

        if img != previous_image:
            return img
        time.sleep(1)
