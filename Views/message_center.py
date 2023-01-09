from tkinter import *


class Message_box():

    def __init__(self , window_x , window_y) -> None:
        self.messagebox  =Tk()
        # self.messagebox.title("Library Manager - Notification")
        self.x = window_x + 10
        self.y = window_y + 10
        self.messagebox.geometry("300x100+%d+%d" %(self.x , self.y))
        self.messagebox.overrideredirect(True)
        self.messagebox.config(bg='white')


    def running_app(self):
        self.messagebox_label = Message(self.messagebox , text="Lorem ipsum dolor sit amet, consectetur adipiscing eland this has to be donefor the  main part in the eantine " , bg='white')
        self.messagebox_label.config(width=290 , padx=10 , pady=10)
        self.messagebox_label.pack()
        self.destroy_btn  = Button(self.messagebox , text="Close Notification" , width=30 ,bg='white' , command=lambda : self.messagebox.destroy()).pack()
        self.messagebox.mainloop()


if __name__ == '__main__':
    name  = Message_box(10, 10)
    name.running_app()