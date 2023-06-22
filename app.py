from flask import Flask, render_template
from gevent.pywsgi import WSGIServer
import tkinter as tk
import pyautogui
import threading


app = Flask(__name__)

def run_tkinter():
    # Create and configure the Tkinter root window
    root = tk.Tk()
    root.attributes("-fullscreen", True, "-topmost", True)
    root.overrideredirect(True)

    # Hide the cursor
    root.config(cursor="none")

    # Disable mouse events (same as before)
    root.bind('<Motion>', lambda event: root.event_generate('<<Motion>>'))
    root.bind('<Button>', lambda event: root.event_generate('<<Button>>'))
    root.bind('<Double-Button>', lambda event: root.event_generate('<<Double-Button>>'))
    root.bind('<Triple-Button>', lambda event: root.event_generate('<<Triple-Button>>'))
    root.bind('<B1-Motion>', lambda event: root.event_generate('<<B1-Motion>>'))
    root.bind('<B2-Motion>', lambda event: root.event_generate('<<B2-Motion>>'))
    root.bind('<B3-Motion>', lambda event: root.event_generate('<<B3-Motion>>'))
    root.bind('<Enter>', lambda event: root.event_generate('<<Enter>>'))
    root.bind('<Leave>', lambda event: root.event_generate('<<Leave>>'))
    root.bind('<MouseWheel>', lambda event: root.event_generate('<<MouseWheel>>'))
    root.bind('<KeyPress>', lambda event: root.event_generate('<<KeyPress>>'))
    root.bind('<KeyRelease>', lambda event: root.event_generate('<<KeyRelease>>'))

    # Capture the screen
    screen = pyautogui.screenshot()

    # Create a label with the captured screen image
    label = tk.Label(root)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Add "Hello Moto" label in the center
    hello_label = tk.Label(root, text="Hello Moto", font=("Arial", 24))
    hello_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    time_interrupt = 100000000000  # Time screen is active in ms
    root.after(time_interrupt, root.destroy)

    root.mainloop()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    tkinter_thread = threading.Thread(target=run_tkinter)
    tkinter_thread.start()

    server = WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
