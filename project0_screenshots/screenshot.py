import datetime, pyautogui, time
from tkinter import *


def screenshot():
    window.iconify()
    time.sleep(0.2)
    e=datetime.datetime.now()
    path = f"D:/python/projects20/pythonProject1/project0/screenshots/image-{e.day}-{e.hour}-{e.minute}-{e.second}.jpg"
    img = pyautogui.screenshot(path)
    img.show()
    window.deiconify()


window = Tk()
window.geometry("300x150")
window.title("Screenshot")
window.config(background="black")
button=Button(window,text="Take A Screenshot", command=screenshot,bg="#ff0000")
button.config(padx=15,pady=15, font=("Ink Free",15,"bold"))
button.pack()
quit=Button(window,text="Quit",command=window.destroy)
quit.pack()
window.mainloop()


