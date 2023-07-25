import tkinter as tk
import json
import pyperclip
import time
import threading
import pyautogui
import keyboard

def search(event=None):
    search_query = entry.get()

    with open('word.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    results = data['results']

    for button in result_buttons:
        button.destroy()

    for result in results:
        if result.startswith(search_query): 
            button = tk.Button(result_frame, text=result, command=lambda text=result: copy(text))
            button.pack()
            result_buttons.append(button) 

    entry.delete(0, tk.END) 

def copy(text):
    pyperclip.copy(text)

    threading.Thread(target=move).start()

    entry.delete(0, tk.END)  

def move():
    x, y = 558, 770 #끄투리오 기준 타이핑박스 좌표입니다. 다른곳에 사용하시려면 수정하세요.
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
    pyautogui.click()

    text = pyperclip.paste()
    keyboard.write(text)
    time.sleep(0.1)
    pyautogui.press('enter')

window = tk.Tk()
window.title("lanier")
window.attributes('-topmost', True)

entry = tk.Entry(window, width=30)
window.resizable(width=False, height=False)
entry.pack(pady=10)
entry.bind("<Return>", search)  

result_frame = tk.Frame(window)
result_frame.pack(pady=10)

search_button = tk.Button(window, text="검색", command=search)
search_button.pack()

result_buttons = []

window.mainloop()
