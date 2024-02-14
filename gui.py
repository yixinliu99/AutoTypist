import tkinter as tk
import threading
import time

def start_in_3_seconds():
    time.sleep(3)
    print("Starting...")

def start_thread():
    global thread
    thread = threading.Thread(target=start_in_3_seconds)
    thread.start()

def stop_thread():
    global thread
    if thread is not None and thread.is_alive():
        thread.join()
        print("Stopped.")



def main():
    # Create the main window
    root = tk.Tk()
    root.title("Text Input and Buttons")

    # Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the window width and height to occupy 20% of the screen
    window_width = int(screen_width * 0.2)
    window_height = int(screen_height * 0.4)

    # Set the window dimensions and position it in the center of the screen
    root.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

    # Configure rows and columns to resize proportionally
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create and position the "Paste text here" label
    paste_label = tk.Label(root, text="Paste text here", font=("Helvetica", 16))
    paste_label.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="ew")

    # Create and position the text input
    text_input = tk.Entry(root, font=("Helvetica", 256), width=20)  # Increase font size here
    text_input.grid(row=1, column=0, columnspan=2, pady=(0, 5), padx=10, sticky="ew")

    # Create and position the "Start in 3 seconds" button
    start_button = tk.Button(root, text="Start in 3 seconds", command=start_thread, font=("Helvetica", 16))
    start_button.grid(row=2, column=0, pady=5, padx=10, sticky="ew")

    # Create and position the "Stop" button
    stop_button = tk.Button(root, text="Stop", command=stop_thread, font=("Helvetica", 16))
    stop_button.grid(row=2, column=1, pady=5, padx=10, sticky="ew")

    # Initialize thread variable
    thread = None

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
