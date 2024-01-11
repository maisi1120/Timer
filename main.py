from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F875AA"
RED = "#e7305b"
GREEN = "#176B87"
GRAY = "#04364A"
BLUE = "#164863"
WHITE = "#FCF5ED"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    global reps
    reps = 0

    window.after_cancel(timer)
    time_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        time_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        time_label.config(text="Work", fg=WHITE)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        # Solution 1
        for _ in range(work_session):
            marks += "😎"
        check_label.config(text=marks)
        # Solution 2
        # if reps % 2 == 0:
        #     check_label["text"] += "😎"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=150, bg=GRAY)

canvas = Canvas(width=200, height=224, bg=GRAY, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")

time_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=GRAY, fg=GREEN)
time_label.grid(column=1, row=0)

check_label = Label(bg=GRAY)
check_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightbackground=GRAY, command=start_timer, width=8, height=1)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=GRAY, command=reset_timer, width=8, height=1)
reset_button.grid(column=2, row=2)

window.mainloop()

