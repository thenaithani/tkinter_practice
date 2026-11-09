import tkinter
from importlib.metadata import pass_none
from tkinter import Label

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
time = 5
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reset_true = False

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_command():
    global reset_true
    reset_true = False
    countdown(time)

def reset_command():
    global time
    global reset_true
    reset_true = True
    time = 5
    canvas.itemconfig(timer_number, text=time)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time):
    canvas.itemconfig(timer_number, text=str(time))
    if time > 0 and reset_true != True:
        window.after(1000, countdown, time - 1)



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
label_text = tkinter.Label(text="Timer", font=(FONT_NAME,40),bg=YELLOW, fg=GREEN, highlightthickness=0)
label_text.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", command=start_command)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_command)
reset_button.grid(column=2, row=2)

verification = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME,30))
verification.grid(column=1, row=3)

window.config(padx=80,pady=60, bg=YELLOW)
canvas = tkinter.Canvas(width=200, height=223,bg=YELLOW, highlightthickness=0)

tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,110, image=tomato)
timer_number = canvas.create_text(102,112, text=str(time), fill="white", font=(FONT_NAME, 40))

canvas.grid(column=1, row=1)


window.mainloop()