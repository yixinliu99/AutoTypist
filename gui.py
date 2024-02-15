import tkinter as tk
from tkinter import filedialog, scrolledtext
import multiprocessing
import time
from typist import Typist

class GUI:
    def __init__(self):
        self.file_path = None


    def typing(self, text, interval):
        typist = Typist()
        delay = int(3)
        time.sleep(delay)
        if self.file_path:
            typist.run_from_file(self.file_path, interval)
        else:
            typist.run(text, interval)


    def start_typing(self):
        global t1
        text = txt_box.get("1.0", tk.END)[:-1] if not self.file_path else None
        t1 = multiprocessing.Process(target=self.typing,
                                     args=(text, ent_interval.get()))
        t1.start()
        message_label.config(text="Typing will start in 3 seconds!", fg="green")


    def choose_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            txt_box.config(state=tk.DISABLED, fg='grey')  # Disable text box and change text color to grey
            message_label.config(text="File chosen successfully!", fg="green")


    def run(self):
        global window, frm_params, ent_interval, txt_box, frm_buttons, message_label

        window.title("Auto Typist")

        # Buttons Frame
        frm_buttons = tk.Frame()
        frm_buttons.grid(row=5, column=0)

        # Start
        start = tk.Button(text="Start (in 3 seconds)", master=frm_buttons, command=lambda: self.start_typing())
        start.grid(row=0, column=0, padx=10, pady=10)

        # Choose from file
        choose_file_button = tk.Button(text="Choose from file", master=frm_buttons, command=self.choose_file)
        choose_file_button.grid(row=0, column=1, padx=10, pady=10)

        # Text Box
        txt_box = scrolledtext.ScrolledText(window, undo=True)
        txt_box.insert(tk.INSERT, "Paste Text Here Or Choose From File...")
        txt_box.grid(row=4, column=0, pady=(10, 2))

        # Message label
        message_label = tk.Label(window, text="", fg="green")
        message_label.grid(row=6, column=0, pady=5)

        # Params Frame
        frm_params = tk.Frame()
        frm_params.grid(row=0, column=0)

        # Interval
        lbl_interval = tk.Label(text="Waiting interval between characters (in seconds)", master=frm_params)
        lbl_interval.grid(row=0, column=1, padx=50, pady=5)

        ent_interval = tk.Entry(justify='center', master=frm_params)
        ent_interval.insert(0, "0.00")
        ent_interval.grid(row=2, column=1, padx=50)

        window.mainloop()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    window = tk.Tk()
    gui = GUI()
    gui.run()
