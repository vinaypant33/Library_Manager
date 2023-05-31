from tkinter import *
from tkinter import messagebox



def info_messagebox(message_string):
    messagebox.showinfo("Library Manager" , message_string)

def error_messagebox(message_string):
    messagebox.showerror("Library Manager" , message_string)

def warning_messagebox(message_string):
    messagebox.showwarning("Library Manager" , message_string)