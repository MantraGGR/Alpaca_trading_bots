import tkinter

class GUI():
    def __init__(self, root):
        self.root= root
        self.root.title = "0603 Asset Management"


        self.form_frame = tk.Frame(root)
        self.form_frame.pack(pady=10)
        