import tkinter as tk
from tkinter import ttk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.title = tk.Label(self, text="Registration Form", font=("Arial", 16))
        self.full_name = tk.Label(self, text="Full Name")
        self.enter_name = tk.Entry(self)
        self.email = tk.Label(self, text="Email")
        self.enter_email = tk.Entry(self)
        self.submit = tk.Button(self, text="Submit")

        self.place_widget()

    def place_widget(self):
        settings = {"stick": "W", "padx": 5, "pady": 5}
        self.rowconfigure(0, weight=11)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)


        self.title.grid(row=0, column=0, rowspan=2, stick=tk.EW)
        self.full_name.grid(row=1, column=0,  **settings)
        self.enter_name.grid(row=1, column=1, **settings)
        self.email.grid(row=2, column=0, **settings)
        self.enter_email.grid(row=2, column=1, **settings)

class GenderFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.gender = tk.Label(self, text="Gender")
        self.selected_gender = tk.StringVar()
        self.genders = ("Male", "Female")

        self.place_widget()

    def place_widget(self):
        settings = {"padx": 5, "pady": 5}
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.gender.grid(row=0, column=0
                         )
        for idx, gender in enumerate(self.genders):
            r = tk.Radiobutton(self, text=gender, variable=self.selected_gender, value=gender)
            r.grid(row=0, column=idx + 1, stick=tk.EW)



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Registration form")
    root.geometry("300x200")
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    gender_frame = GenderFrame(root)
    gender_frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()