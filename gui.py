import tkinter as tk
from tkinter import scrolledtext
import multiprocessing
import time
import sys

def typing(interval, data, typing_function):
    delay = int(3)
    time.sleep(delay)
    typing_function(data, interval)


def start_typing(typing_function):
    global t1
    t1 = multiprocessing.Process(target=typing,
                                 args=(ent_interval.get(), txt_box.get("1.0", tk.END)[:-1], typing_function))
    t1.start()


def stop_typing():
    t1.terminate()
    t1.join()
    sys.stdout.flush()


def select_all(event):
    txt_box.tag_add(tk.SEL, "1.0", tk.END)
    txt_box.mark_set(tk.INSERT, "1.0")
    txt_box.see(tk.INSERT)
    return 'break'


def run(typing_function):
    global window, frm_params, ent_interval, txt_box, frm_buttons

    window = tk.Tk()
    window.title("Auto Typer")

    # Params Frame
    frm_params = tk.Frame()
    frm_params.grid(row=0, column=0)


    # Interval
    lbl_interval = tk.Label(text="Waiting time between characters (In Sec)", master=frm_params)
    lbl_interval.grid(row=0, column=1, padx=50, pady=5)

    ent_interval = tk.Entry(justify='center', master=frm_params)
    ent_interval.insert(0, "0.00")
    ent_interval.grid(row=1, column=1, padx=50)

    # Data
    lbl_data = tk.Label(text="Paste Text Here", font='Helvetica 18 bold')
    lbl_data.grid(row=3, column=0, pady=(10, 2))

    txt_box = scrolledtext.ScrolledText(window, undo=True)
    txt_box.grid(row=4, column=0)

    txt_box.bind("<Control-Key-a>", select_all)
    txt_box.bind("<Control-Key-A>", select_all)

    # Buttons Frame
    frm_buttons = tk.Frame()
    frm_buttons.grid(row=5, column=0)

    # Start
    start = tk.Button(text="Start (in 3 seconds)", master=frm_buttons, command=lambda: start_typing(typing_function))
    start.grid(row=0, column=0, padx=10, pady=10)

    # Stop
    stop = tk.Button(text="Stop", master=frm_buttons, command=stop_typing)
    stop.grid(row=0, column=1, padx=10, pady=10)

    # Exit
    exit_button = tk.Button(text="Exit", master=frm_buttons, command=window.destroy)
    exit_button.grid(row=0, column=2, padx=10, pady=10)

    window.mainloop()
