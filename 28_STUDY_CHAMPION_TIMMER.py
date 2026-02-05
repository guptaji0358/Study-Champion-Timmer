# Project - Study Champion Timmer
# -------------------------------

from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

# Fast demo time
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10

BG = "#F8FAFC"

WORK_COLOR = "#4F46E5"
BREAK_COLOR = "#06B6D4"
LONG_COLOR = "#EC4899"
CHECK = "#09fb62"

reps = 0
timer = None


# ---------------------------- TIMER ------------------------------- #
def start_timmer_with_button():
    global reps, timer
    if timer:
        window.after_cancel(timer)

    reps += 1

    work_sec = int(WORK_MIN * 60)
    short_sec = int(SHORT_BREAK_MIN * 60)
    long_sec = int(LONG_BREAK_MIN * 60)

    if reps % 8 == 0:
        Timmer_Label.config(text="LONG BREAK", fg=LONG_COLOR)
        countown_timmer(long_sec)

    elif reps % 2 == 0:
        Timmer_Label.config(text="BREAK", fg=BREAK_COLOR)
        countown_timmer(short_sec)

    else:
        Timmer_Label.config(text="WORK", fg=WORK_COLOR)
        countown_timmer(work_sec)


def countown_timmer(count):
    global timer
    m = count // 60
    s = count % 60

    if s < 10:
        s = f"0{s}"

    canvas.itemconfig(Timmer_Text, text=f"{m}:{s}")

    if count > 0:
        timer = window.after(1000, countown_timmer, count - 1)

    else:
        check_mark.config(text="✔" * (reps // 2))
        start_timmer_with_button()

# ---------------------------- RESET ------------------------------- #
def reset_timer():
    global reps, timer
    if timer:
        window.after_cancel(timer)

    reps = 0
    timer = None
    Timmer_Label.config(text="TIMER", fg=WORK_COLOR)
    canvas.itemconfig(Timmer_Text, text="00:00")
    check_mark.config(text="")


# ---------------------------- CLOSE ------------------------------- #
def close_app():
    window.destroy()

# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Study Champion Timer")
window.config(padx=40, pady=30, bg=BG)

top_frame = Frame(window, bg=BG)
top_frame.pack(fill="x")

Timmer_Label = Label(top_frame,text="TIMER",font=(FONT_NAME, 38, "bold"),fg=WORK_COLOR,bg=BG)
Timmer_Label.pack(side="left", padx=10)

exit_button = Button(top_frame,text="Exit",command=close_app)
exit_button.pack(side="right", padx=10)

canvas = Canvas(window,width=230,height=230,bg=BG,highlightthickness=0)
canvas.pack(pady=20)


tomato_img = PhotoImage(file=r"E:\Program Files\RobinData\PYTHON\RawData\TOMATO.png")
canvas.create_image(115, 115, image=tomato_img)

Timmer_Text = canvas.create_text(115, 130,text="00:00",fill="white",font=(FONT_NAME, 30, "bold"))

button_frame = Frame(window, bg=BG)
button_frame.pack(pady=10)

start_button = Button(button_frame,text="Start",command=start_timmer_with_button,width=8)
start_button.grid(row=0, column=0, padx=10)

check_mark = Label(button_frame,text="",font=(FONT_NAME, 18, "bold"),fg=CHECK,bg=BG,width=6)
check_mark.grid(row=0, column=1)

reset_button = Button(button_frame,text="Reset",command=reset_timer,width=8)
reset_button.grid(row=0, column=2, padx=10)

window.mainloop()