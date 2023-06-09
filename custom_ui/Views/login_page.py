import time 
import tkinter as tk 
from tkinter import messagebox 
from PIL import Image, ImageTk
import colors 
import styles


from pubsub import pub  # For Message Passing b/w the modules



class Login_page():

    def __init__(self , width  , height ) -> None:
        self.loginscreen  = tk.Tk()
        self.loginscreen.overrideredirect(True)
        self.screenheight  = self.loginscreen.winfo_screenheight()
        self.screenwidth  = self.loginscreen.winfo_screenwidth()
        self.height  =  height
        self.width  = width
        self.ycoordinate = (self.screenheight // 2) - (self.height //2 )
        self.xcoordinate = (self.screenwidth //2 ) - (self.width //2 )
        self.loginscreen.geometry(f"{self.width}x{self.height}+{self.xcoordinate}+{self.ycoordinate}")
        self.loginscreen.configure(background=colors.login_page_base)



    ## Image Manipulation and Some other basic calculations 
        _user_image  = Image.open(r"Assets\user.png")
        resized_image_user  = _user_image.resize((150,150))
        self.user_image  = ImageTk.PhotoImage(resized_image_user)

    ## App Functions
    def mouse_click(self, event):
        self.x  = event.x
        self.y = event.y 

    def move_window(self, event):
        self.delta_x  = event.x  - self.x 
        self.delta_y =  event.y - self.y 
        self.new_x  = self.loginscreen.winfo_x() + self.delta_x
        self.new_y = self.loginscreen.winfo_y() + self.delta_y
        self.loginscreen.geometry(f"{self.width}x{self.height}+{self.new_x}+{self.new_y}")
    
    def closing_app(self):
        self.loginscreen.destroy()


        # Check Username and Password.
    def login_button_clicked(self):
        self.username , self.password  = self.username_box.get() , self.password_box.get()
        self.username_box.delete(0 , 'end')
        self.password_box.delete(0 , 'end')
        pub.sendMessage('login_details' , user_details = self.username + ',' + self.password)

    def calling_register(self , event):
        pub.sendMessage('register_page_called' , register_data  = "Data")


    ## Section for control definition and placement
    def defining_controls(self):
        ## Titlebar and Closing Button
        self.titlebar  = tk.Frame(self.loginscreen , background=colors.login_page_base , height=18)
        self.titlebar.pack_propagate(1)
        self.closing_button  = tk.Button(self.titlebar , text=" X " , command=self.closing_app)
        ## User Image : 
        self.user_image_label  = tk.Label(self.loginscreen , image=self.user_image , background=colors.login_page_base)
        ## Username Password and Login Button : 
        self.username_box = tk.Entry(self.loginscreen)
        self.username_line   =tk.Frame(self.loginscreen)
        self.password_box  = tk.Entry(self.loginscreen)
        self.password_line   = tk.Frame(self.loginscreen)
        self.login_button  =tk.Button(self.loginscreen , text="LOGIN" , command=self.login_button_clicked)
        ## Sign IN and forgot password
        self.donthaveaccount_text = tk.Label(self.loginscreen , text="Don't Have an Account ?")
        self.signin_text = tk.Label(self.loginscreen  , text="Sign In !")
        self.forgot_password_text  = tk.Label(self.loginscreen , text="Forgot Password ?")
        ## Section for configuring the controls
        self.username_box.insert(0 ,  "Username")
        self.password_box.insert(0 , "Password")
        self.loginscreen.configure(background=colors.login_page_base)
        self.closing_button.configure(styles.tkinter_styles.button_style_login(self, self.closing_button))
        self.username_box.configure(styles.tkinter_styles.textbox_configure(self , self.username_box))
        self.username_line.configure(styles.tkinter_styles.login_line_configure(self , self.username_line))
        self.password_box.configure(styles.tkinter_styles.textbox_configure(self, self.password_box))
        self.password_line.configure(styles.tkinter_styles.login_line_configure(self, self.password_line))
        self.login_button.configure(styles.tkinter_styles.button_style_login(self , self.login_button))
        self.login_button.configure(height=2 , width=10 , justify="center" , relief="sunken",
                                    border=0 , foreground=colors.login_page_base , background=colors.login_button_color , activeforeground=colors.red_color,
                                    activebackground=colors.login_page_purple , font=styles.small_font_bold)
        self.signin_text.configure(foreground=colors.red_color)
        self.forgot_password_text.configure(foreground=colors.red_color)
        ## Section for binding the controls 
        self.titlebar.bind("<Enter>" , lambda event : styles.tkinter_styles.change_color_on_hover(self , self.titlebar , colors.login_button_color))
        self.titlebar.bind("<Leave>" , lambda event : styles.tkinter_styles.change_color_on_hover(self , self.titlebar , colors.login_page_base))
        self.titlebar.bind("<ButtonPress-1>" , self.mouse_click)
        self.titlebar.bind("<B1-Motion>" , self.move_window)
        self.username_box.bind("<FocusIn>" , lambda event :  styles.tkinter_styles.textbox_hover(self,  self.username_box , self.password_box))
        self.password_box.bind("<FocusIn>" , lambda event : styles.tkinter_styles.textbox_hover(self,  self.password_box , self.password_box))
        self.signin_text.bind("<Enter>" , lambda event :  styles.tkinter_styles.change_foreground_hover(self ,self.signin_text , colors.black_color))
        self.signin_text.bind("<Leave>" , lambda event : styles.tkinter_styles.change_foreground_hover(self, self.signin_text , colors.red_color))
        self.forgot_password_text.bind("<Enter>" , lambda event : styles.tkinter_styles.change_foreground_hover(self, self.forgot_password_text , colors.black_color))
        self.forgot_password_text.bind("<Leave>" , lambda event : styles.tkinter_styles.change_foreground_hover(self , self.forgot_password_text , colors.red_color))
        self.signin_text.bind("<ButtonPress-1>" , self.calling_register)
        
    def placing_controls(self):
        self.titlebar.pack(side="top" , fill="x")
        self.closing_button.pack(side="right" , padx=(0 , 0))
        self.user_image_label.pack(side="top" , pady=(10,20))
        self.username_box.pack(side="top"  , fill='x' ,padx=(10, 10))
        self.username_line.pack(side="top" ,fill="x" , padx=(10,10))
        self.password_box.pack(side="top"  , fill="x" , padx=(10,10))
        self.password_line.pack(side="top" , fill="x" , padx=(10,10))
        self.login_button.pack(side="top" , pady=(25,2) , fill="x" , padx=(10,10))
        self.donthaveaccount_text.pack(side="left" , pady = (0 , 2) , padx=(2,2))
        self.signin_text.pack(side="left" , pady=(2 , 2))
        self.forgot_password_text.place(x=2 , y=410)
        ## Calling the main app loop  : 
        self.loginscreen.mainloop()


if __name__  == '__main__':
    loginscreen  = Login_page(300 , 450)
    loginscreen.defining_controls()
    loginscreen.placing_controls()
