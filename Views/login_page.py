import tkinter as tk
from tkinter import messagebox


## Importing from app made modules
from colors import *



class Login_page():
    

    def __init__(self, master, width, height) -> None:
        self.master  = tk.Tk()
        self.app_width = width 
        self.app_height  = height
        self.current_height  = self.master.winfo_height()
        self.current_width  = self.master.winfo_width()
        self.current_location_x  = (self.app_width //2 ) - (self.current_width // 2)
        self.current_location_y = (self.app_height //2 ) - (self.current_height //2)
        self.master.configure(background=login_page_base)
        self.master.geometry(f"{self.app_width}x{self.app_height}+{self.current_location_x}+{self.current_location_y}")
        self.master.overrideredirect(True)

    ## defining the app related initial functions here

    def defining_controls(self):
        self.upper_control  = tk.Frame(self.master , background='Black')

    def placing_controls(self):


        self.upper_control.pack()
        self.master.mainloop()



## Dummy calling for the login_page 
if __name__ == '__main__':
    login = Login_page(master = "hehe" , width=500 , height=300)
    login.defining_controls()
    login.placing_controls()
