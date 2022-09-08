import tkinter as ui
import time


window = ui.Tk()


def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    digital_clocklbl.config(text=time_text)
    # 1000 miliseconds equal 1 second, hence the updizzle
    digital_clocklbl.after(1000, update_clock)


digital_clocklbl = ui.Label(window, text="00.00.00",
                            font="Helvetica 72 bold")
digital_clocklbl.pack()


update_clock()

window.mainloop()
