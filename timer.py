# This project is used for timers purpose. For eg you are working for some hours so this software will give you break after each 20 minutes for  5 minutes and after sometime it will give you break for 25 mins

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
after_id = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global after_id
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(id=after_id)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # This means 25 minutes because the function down takes argument in the form of seconds
    countdown(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time):
    global after_id
    # Its the logic to display the time and seconds as the stopwatch if ou dont understand this logic than just open the calculator and modulo calculator and start from 5*60 which we had passed in start_timer() function

    # We are using floor function because after dividing we dont our result in point
    minutes = math.floor(time / 60)
    seconds = time % 60

    # This two lines of codes will add '0' in before the single digit number for eg when the seconds are 10 then after '10' '9' will come but we want to show '09' and not only '9' so this two lines of code will be helpful. If you dont understand this 2 lines of code then just comment it and see the results
    if len(str(seconds)) == 1:
        seconds = f"0{str(seconds)}"

    if len(str(minutes)) == 1:
        minutes = f"0{str(minutes)}"

    # This line is used to change the text that we had set for the canvas that is 00:00
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if(time > 0):
        after_id = window.after(1000, countdown, time-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Timer (Pomodoro)")
# This method is used for giving padding from all the sides
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer",  fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# This line is used to create the canvas 'highlightthickness=0' is used to hide the border which will be displayed when we apply the background color on the canvas and we use canvas to paste the image on it
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")

# In the image parameter we cant directly give the file name because it accepts the file in the "PhotoImage" format which we had created in the above line
canvas.create_image(100, 112, image=tomato_image)
# Writing the line that will be displayed on the canvas on the image. `fill="white"` --> changes the color of the font
# font=() --> this font attribute will be in the form  of the tuple the first element in the tuple is the font_name, second argument is the font size and the third argument specifies the boldness of the text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()