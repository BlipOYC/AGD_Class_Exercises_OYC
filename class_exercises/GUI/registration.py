import tkinter as tk
from tkinter import ttk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.title = tk.Label(self, text="Registration Form")
        self.full_name = tk.Label(self, text="Full Name")
        self.enter_name = tk.Entry(self)
        self.email = tk.Label(self, text="Email")
        self.enter_email = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit")

        self.place_widget()

    def place_widget(self):
        self.title.pack(side=tk.LEFT)
        self.full_name.pack(side=tk.LEFT)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Registration form")
    root.geometry("300x200")
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()