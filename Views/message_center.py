from tkinter import *








class Message_box():

    def __init__(self) -> None:
        self.messagebox  =Tk()
        # self.messagebox.title("Library Manager - Notification")
        self.messagebox.geometry("300x300+300+300")
        self.messagebox.overrideredirect(True)


    def running_app(self):
        self.messagebox_label = Message(text="hello world this is an amazing day tpday adn i have been working for the main character sfor the main series in the meantime ")
        self.messagebox_label.config(width=290 , padx=10 , pady=10)
        self.messagebox_label.pack()
        self.destroy_btn  = Button(self.messagebox , text="Close Notification" , width=30 , command=lambda : self.messagebox.destroy()).pack()
        self.messagebox.mainloop()




name = Message_box()
name.running_app()