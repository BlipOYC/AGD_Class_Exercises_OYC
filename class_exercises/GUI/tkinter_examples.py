import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.txt = tk.Label(self, text="Hello tkinter", bg="seagreen2", fg="orangered4")
        self.btn = tk.Button(self, text="Click Me", bg="ivory4", fg="darkgoldenrod", activebackground="pink")
        self.sld = tk.Scale(self, from_=0, to=100, orient=tk.VERTICAL, bg = "darkslategrey", fg = "magenta2")
        self.edt = tk.Entry(self, bg = "slateblue3", fg = "white")

        self.place_widget()

        #Changes configuration of existing widget
        self.config(bg="lemonchiffon")

    def place_widget(self):
        self.txt.grid(column=0, row=0, padx=10, pady=10)
        self.btn.grid(column=1, row=1, padx=10, pady=10)
        self.sld.grid(column=2, row=2, padx=10, pady=10)
        self.edt.grid(column=3, row=3, padx=10, pady=10)



if __name__ == '__main__':
    root = tk.Tk()

    root.title("Tkinter Class Example")
    main_frame = MainFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()