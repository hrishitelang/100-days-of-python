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
reps = 1
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    while reps < 9:
        if reps in [1, 3, 5, 7]:
            count_down(25*60)
        elif reps in [2, 4, 6]:
            count_down(5*60)
        elif reps == 8:
            count_down(20*60)
        reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count/60)
    count_second = count % 60
    if count_second == 0:
        count_second = "00"
    elif count_second in range(1,10):
            count_second = "0"+str(count_second)
    canvas.itemconfig(timer_number, text=f'{count_minute}:{count_second}')
    if count > 0:
        window.after(1000, count_down, count-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Application")
window.config(padx=100, pady=50,bg=YELLOW)


timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 38))
timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_number = canvas.create_text(100, 125, text="00:00", fill=YELLOW, font=(FONT_NAME, 34, 'bold'))
canvas.grid(row=1, column=1)


start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset")
reset.grid(row=2, column=2)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

window.mainloop()