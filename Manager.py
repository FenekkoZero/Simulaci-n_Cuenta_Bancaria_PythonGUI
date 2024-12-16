import tkinter as tk
from constants import style
from screens import home, login, deposit, withdraw

#crear clase manager
class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Simulación Cuenta Bancaria")
        container = tk.Frame(self)
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )
        container.configure(background = style.home_backg)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        
        self.frames = {}
        for F in (login, home, deposit, withdraw):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.show_frame(login)   

    
    def show_frame(self, container):
        frame = self.frames[container]
        if hasattr(frame, "update_saldo"):  # Si el Frame tiene update_saldo
            frame.update_saldo()
        frame.tkraise()