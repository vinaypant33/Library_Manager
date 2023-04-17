import tkinter as tk
from tkinter import messagebox
## Importing from app made modules
from colors import *



class Login_page():
    

    def __init__(self, master, width, height) -> None:
        self.loginscreen  = tk.Tk()
        self.loginscreen.overrideredirect(True)
        self.screenheight  = self.loginscreen.winfo_screenheight()
        self.screenwidth  = self.loginscreen.winfo_screenwidth()
        self.height  =  height
        self.width  = width
        self.ycoordinate = (self.screenheight // 2) - (self.height //2 )
        self.xcoordinate = (self.screenwidth //2 ) - (self.width //2 )
        self.loginscreen.geometry(f"{self.width}x{self.height}+{self.xcoordinate}+{self.ycoordinate}")
        self.loginscreen.configure(background='White')

    ## defining the app related initial functions here
    def defining_controls(self):
        # Upper Control
        self.upper_control  = tk.Frame(self.loginscreen , background=login_page_base ,  height=20)
        self.upper_control.pack_propagate(1)
        # Base Controls : Login icon 
        

    def placing_controls(self):

        self.upper_control.pack(side='top' , fill='x')
        self.loginscreen.mainloop()



## Dummy calling for the login_page 
if __name__ == '__main__':
    login = Login_page(master = "hehe" , width=500 , height=300)
    login.defining_controls()
    login.placing_controls()
