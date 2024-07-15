import webbrowser
import time 
import pyautogui

urls = [
    "https://www.youtube.com",
    "https://www.google.com",
    "https://github.com/maverik-io/joe-web-refresher",
]

def open_urls(urls):
    for url in urls:
        webbrowser.open(url)


def refresh_page():
    pyautogui.hotkey('ctrl','tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(1)

def go_back():
    pyautogui.hotkey('ctrl','shift','tab')


if __name__ == "__main__":
    open_urls(urls)
    while True:
        for i in range(len(urls)):
            refresh_page()

        for i in range(len(urls)):
            go_back()
