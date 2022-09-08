
from ssl import _create_unverified_context
import tkinter as ui
import time
import math

window = ui.Tk()
window.geometry("400x400")


def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")

    # Updating seconds hand

    seconds_x = seconds_hand_len * \
        math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = seconds_hand_len * \
        math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    # Updating Minutes Hand

    minutes_x = minutes_hand_len * \
        math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = minutes_hand_len * \
        math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # Updating hours Hand
    hours_x = hours_hand_len * \
        math.sin(math.radians(hours * 30 + .05 *
                 minutes + 0.008 * seconds)) + center_x
    hours_y = -1 * hours_hand_len * \
        math.cos(math.radians(hours * 30 + .05 *
                 minutes + 0.008 * seconds)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    # 1000 miliseconds equal 1 second, hence the updizzle
    window.after(1000, update_clock)


canvas = ui.Canvas(window, width=400, height=400, bg="black")
canvas.pack(expand=True, fill='both')

# create background
bg = ui.PhotoImage(file='blank_clock.png')
canvas.create_image(640, 640, image=bg)

# Create clock hands
center_x = 200
center_y = 200

seconds_hand_len = 95
minutes_hand_len = 80
hours_hand_len = 60

# Second hand
seconds_hand = canvas.create_line(
    200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='red')
# Minutes hand
minutes_hand = canvas.create_line(
    200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='white')
# Hours hand
hours_hand = canvas.create_line(
    200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='white')


update_clock()

window.mainloop()
