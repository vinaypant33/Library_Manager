import tkinter
from tkinter.ttk import *
from tkinter import *
from pubsub import pub



""" part to be used for placing the window in specific location """

"""
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
"""

class LoginScreen():
    def __init__(self) -> None:
        self.loginscreen  =Tk()
        self.loginscreen.title("Library Manager")
        self.loginscreen.geometry("250x160")
        self.loginscreen.resizable(0,0)
        self.loginscreen.configure(bg='white')
        self.loginscreen.eval('tk::PlaceWindow . center')
        # Setting controls for the main window 
        # Calling the functions for setting and 
        # self.defining_controls()
        # self.placing_controls()

    # Functions to be called when a button is clicked
    def login_clicked(self):
        self.username  = self.username_textbox.get()
        self.password   =self.password_textbox.get()
        self.username_textbox.delete(0 , 'end')
        self.password_textbox.delete( 0 , 'end')
        pub.sendMessage('login_data', login_data = self.username + "," + self.password)
        
    def register_clicked(self):
        pub.sendMessage('register_clicked')

    def forgot_clicked(self, e):
        pub.sendMessage("forgot_clicked")

    def defining_controls(self):
        self.usrname_label = Label(self.loginscreen , text="Enter Username :" , bg='white')
        self.username_frame  = Frame(self.loginscreen , width=228 , height=2 , bg='black')
        self.password_label  = Label(self.loginscreen , text="Enter Password :" , bg='white')
        self.password_frame  =  Frame (self.loginscreen, width=228 , height=2 , bg='black')
        self.forgot_password   = Label(self.loginscreen , text="Forgot Password !!" , fg='blue' , bg='white')
        self.username_textbox  = Entry(self.loginscreen , width=37 , border=0)
        self.password_textbox  = Entry(self.loginscreen , show="*" , width=37 , border=0)
        self.login_btn = Button(self.loginscreen , text="Client Login" , width=14 , bg='white' , command=self.login_clicked)
        self.register_btn  =Button(self.loginscreen , text="Client Register" , width=14 , bg='white' , command=self.register_clicked)
        # Binding function for the label 
        self.forgot_password.bind("<Button>" , self.forgot_clicked)

    def placing_controls(self):
        self.usrname_label.place(x=10 , y=10)
        self.username_textbox.place(x=10 , y=30)
        self.username_frame.place(x=10 ,y=50)
        self.password_label.place(x=10 , y =60)
        self.password_textbox.place(x=10 , y=80)
        self.password_frame.place(x=10 , y=98)
        self.login_btn.place(x=10 , y=105)
        self.register_btn.place(x=130 , y=105)
        self.forgot_password.place(x=80 , y=135)
        # Calling the main function
        self.loginscreen.mainloop()
    
    def killing_app(self):
        self.loginscreen.destroy()


class RegisterScreen():

    def __init__(self) -> None:
        self.register_screen = Tk()
        self.register_screen.title("Register - LM")
        self.register_screen.geometry("260x150")
        self.register_screen.resizable(0,0)
        self.register_screen.configure(bg='white')
        self.register_screen.eval('tk::PlaceWindow . center')
        
        # Defining other data for the form to run
        self.secret_questions  = ["First Pet Name" , "First School Name" , "First Holiday Place" ]

        # Defining the string var for the options menu 
        self.secret_string  = StringVar()
        self.secret_string.set("Choose Secret Question")
        
        # Defining the frame width and height to be shown under the controls
        self.width  = 241
        self.height  = 2

        # Calling the defining and placing controls for the ap
        # self.define_controls()
        # self.place_controls()


    # Functions to delete the pre inserted text when in focus
    def delete_username_text(self , e):
        self.username_textbox.delete(0 , "end")
        self.username_textbox.configure(fg='black')

    def delete_password_text(self, e):
        self.password_textbox.delete(0 , "end")
        self.password_textbox.configure(fg='black' , show="*")

    def delete_secret_textbox(self , e):
        self.secretanswer_textbox.delete(0 , "end")
        self.secretanswer_textbox.config(bg='white' , fg='black')
    
    def secret_question_optionmenu(self, e):
        self.secret_question.configure(bg='white' , fg='black')

    def button_focus(self, e):
        self.registerbtn.configure(fg='blue')
        
    def register_button_clicked(self):
        self.username  = self.username_textbox.get()
        self.username_textbox.delete(0 , "end")
        self.password = self.password_textbox.get()
        self.password_textbox.delete(0 , "end")
        self.secretanswer = self.secretanswer_textbox.get()
        self.secretanswer_textbox.delete(0 , "end")
        # print(self.username , self.password, self.secretanswer)
        pub.sendMessage("register_data" , register_data = self.username + ',' + self.password + ',' +  self.secretanswer)

    def login_button_clicked(self):
        pub.sendMessage("show_login")


    # Defining the static controls in the app
    def define_controls(self):
        self.username_textbox = Entry(self.register_screen , width=40 , border=0 , fg='grey')
        self.username_frame = Frame(self.register_screen ,width=self.width  ,height=self.height , bg='black')
        self.password_frame = Frame (self.register_screen ,width=self.width , height=self.height ,bg='black')
        self.username_textbox.insert(0, "Enter Username")
        self.password_textbox = Entry(self.register_screen , width=40 , border=0 , fg='grey')
        self.password_textbox.insert(0 , "Enter Password")
        self.secretqueston_label  = Label(self.register_screen,  text="Please Select a Secret Question")

        self.secret_question = OptionMenu(self.register_screen , self.secret_string , *self.secret_questions) # Will check and make the options available for the options menu soo
        self.secret_question.configure(bg='white' , fg='black' , border=0)

        # OptionMenu(self.main_layout , self.var_choose, *self.to_take_books)
        # self.secretanswer = Label(self.register_screen , text="Please Inser the answer")
        self.secretanswer_textbox = Entry(self.register_screen,width=40 , border= 0  , fg='grey')
        self.secretanswer_textbox.insert(0 , "Enter Secret Answer" )
        self.secret_answer_frame = Frame(self.register_screen , width=self.width , height=self.height ,bg ='black')
        self.registerbtn = Button(self.register_screen , text="Register New Client" , width=15 , border=2 , fg='black' , bg='white' , command=self.register_button_clicked)
        self.login_button = Button(self.register_screen , text="User Login" , width=15 , border=2 , fg='black' , bg='white' , command=self.login_button_clicked)

        self.username_textbox.bind("<FocusIn>", self.delete_username_text)
        self.password_textbox.bind("<FocusIn>", self.delete_password_text)
        self.secretanswer_textbox.bind("<FocusIn>" , self.delete_secret_textbox)
        self.secret_question.bind("<FocusIn>" ,self.secret_question_optionmenu )
        self.registerbtn.bind("<FocusIn>" , self.button_focus)

    # 
    def kill_register(self):
        self.register_screen.destroy()

    def place_controls(self):
        self.username_textbox.place(x=10 , y=10)
        self.username_frame.place(x=10 , y =30)
        self.password_textbox.place(x=10 , y=32)
        self.password_frame.place(x=10 , y=50)
        self.secret_question.place(x=9 , y=53) # Done till now
        # self.secretanswer.place(x=10 , y=85)
        self.secretanswer_textbox.place(x=10 , y=90)
        self.secret_answer_frame.place(x=10 , y=108)
        self.registerbtn.place(x=10 , y=115)
        self.login_button.place(x=130 , y=115)

        # Calling the main app ( Register Screen) 
        self.register_screen.mainloop()
        
    def deleting_app(self):
        self.register_screen.destroy()


class ForgotPassword():

    def __init__(self) -> None:
        self.forgotscreen = Tk()
        self.forgotscreen.title("Recover Password")
        self.forgotscreen.geometry("270x150")
        self.forgotscreen.resizable(0,0)
        self.forgotscreen.configure(bg='white')
        self.forgotscreen.eval('tk::PlaceWindow . center')


        # Other data that will be used in the class 
        self.secret_questions  = ["First Pet Name" , "First School Name" , "First Holiday Place" ]

        # Defining the string var for the options menu 
        self.secret_string  = StringVar()
        self.secret_string.set("Choose Secret Question")

        # Calling the control defining and placing controls
        # self.defining_controls()
        # self.placing_controls()

    def delete_username_textbox_text(self , e):
        self.username.delete(0 , "end")
        self.username.configure(fg='black')
    
    def delete_password_textboxtext(self , e):
        self.passwordbox.delete(0 , "end")
        self.passwordbox.configure(fg='black')
    
    def secret_answer_textboxdelete(self ,e):
        self.secretquestionanswer.delete(0 , "end")
        self.secretquestionanswer.configure(fg='black')

    def reterive_button_clicked(self):
        username  = self.username.get()
        secret_answer  = self.secretquestionanswer.get()
        pub.sendMessage("reterive_password" , password_details  = username + "," + secret_answer)
        
    def calling_login(self):
        self.forgotscreen.destroy()
        pub.sendMessage("login_clicked")
        
    
    def setting_password(self , password):
        self.passwordbox.insert(0 ,password)
        self.delete_username_textbox_text()
        self.secret_answer_textboxdelete()
        

    # Part for the subscribing for the upcoming messages
    # pub.subscribe("reterived_password" , setting_password)
    
    # Defining the controls and placing them
    def defining_controls(self):
        self.username = Entry(self.forgotscreen , bg='white' , border=0 ,fg='grey' , width=40)
        self.username.insert(0 , "Enter Username")
        self.usename_frame  =  Frame (self.forgotscreen , width=240 , height=2 , bg='black')
        self.passwordbox = Entry(self.forgotscreen , bg='white' , border = 0 , fg='grey' , width=40)
        self.password_frame  = Frame(self.forgotscreen, width=240 , height=2 , bg='black')
        self.secretquestionanswer = Entry(self.forgotscreen , bg='white' , border=0 ,fg='grey' , width=40)
        self.secretquestionanswer.insert(0 , "Enter Secret Question Answer")
        self.secretquestionframe = Frame(self.forgotscreen , width=240 , height=2 , bg='black')
        self.secretquestionchoice = OptionMenu(self.forgotscreen , self.secret_string , *self.secret_questions)
        self.secretquestionchoice.configure(bg='white' , fg='black' , border=0)
        self.reterivebtn = Button(self.forgotscreen , text="Reterive Password" , width=18 , bg='lightgrey',command=self.reterive_button_clicked)
        self.login_btn = Button(self.forgotscreen , text="Show Login" , width=13 , bg='lightgrey' , command=self.calling_login)


        # Calling functions to change text in case of Focus IN 
        self.username.bind("<FocusIn>", self.delete_username_textbox_text)
        self.passwordbox.bind("<FocusIn>" , self.delete_password_textboxtext)
        self.secretquestionanswer.bind("<FocusIn>" , self.secret_answer_textboxdelete)
        

    def placing_controls(self):
        
        self.username.place(x=10 , y=10)
        self.usename_frame.place(x=10 ,y=29)
        self.secretquestionchoice.place(x = 9 , y=35)
        self.secretquestionanswer.place(x=10 , y=65)
        self.secretquestionframe.place(x=10 , y=83)
        self.reterivebtn.place(x = 10 , y=90)
        self.passwordbox.place(x = 10 , y=118)
        self.password_frame.place(x = 10 , y=138)
        self.login_btn.place(x=150 , y=90)


        # Calling the main app to run 
        self.forgotscreen.mainloop()
        
    def killing_app(self):
        self.forgotscreen.destroy()


    


# if __name__ == '__main__':
#     mainscreen  = ForgotPassword()
#     mainscreen = LoginScreen()
#     mainscreen = RegisterScreen()
