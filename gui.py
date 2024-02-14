import tkinter as tk
from tkinter import scrolledtext
import multiprocessing
import time
from typist import Typist


def typing(interval, data):
    typist = Typist(data, interval)
    delay = int(3)
    time.sleep(delay)
    typist.main(data, interval)


def start_typing():
    global t1
    t1 = multiprocessing.Process(target=typing,
                                 args=(ent_interval.get(), txt_box.get("1.0", tk.END)[:-1]))
    t1.start()


def run():
    global window, frm_params, ent_interval, txt_box, frm_buttons

    window.title("Auto Typist")

    # Buttons Frame
    frm_buttons = tk.Frame()
    frm_buttons.grid(row=5, column=0)

    # Start
    start = tk.Button(text="Start (in 3 seconds)", master=frm_buttons, command=lambda: start_typing())
    start.grid(row=0, column=0, padx=10, pady=10)

    # Exit
    exit_button = tk.Button(text="Exit", master=frm_buttons, command=window.destroy)
    exit_button.grid(row=0, column=2, padx=10, pady=10)

    # Text Box
    txt_box = scrolledtext.ScrolledText(window, undo=True)
    txt_box.insert(tk.INSERT, "Paste Text Here")
    txt_box.grid(row=4, column=0, pady=(10, 2))

    # Params Frame
    frm_params = tk.Frame()
    frm_params.grid(row=0, column=0)

    # Interval
    lbl_interval = tk.Label(text="Waiting interval between characters (in seconds)", master=frm_params)
    lbl_interval.grid(row=0, column=1, padx=50, pady=5)

    ent_interval = tk.Entry(justify='center', master=frm_params)
    ent_interval.insert(0, "0.00")
    ent_interval.grid(row=1, column=1, padx=50)

    window.mainloop()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    window = tk.Tk()
    run()
