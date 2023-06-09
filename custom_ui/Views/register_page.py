import tkinter as tk
from tkinter import messagebox

from PIL import Image ,  ImageTk


class Register_page():
    def __init__(self , width , height) -> None:
        import styles
        import colors
        self.register_page  = tk.Tk()
        self.register_page.overrideredirect(True)
        self.screen_height = self.register_page.winfo_screenheight()
        self.screen_width = self.register_page.winfo_screenwidth()
        self.height = height
        self.width  = width
        self.y_coordinate = (self.screen_height // 2) - (self.height //2 )
        self.x_coordinate = (self.screen_width //2 ) - (self.width //2 )
        self.register_page.geometry(f"{self.width}x{self.height}+{self.x_coordinate}+{self.y_coordinate}")
    
    ## Image Importing and editing for the main register page
        _user_image  = Image.open(r'Assets\user.png')
        resized_image_user  = _user_image.resize((150, 150))
        self.user_image   = ImageTk.PhotoImage(resized_image_user)

    ## Section for all functions
    def mouse_click(self , event ):
        self.x = event.x
        self.y = event.y
    
    def move_window(self, event):
        self.delta_x = event.x - self.x
        self.delta_y = event.y - self.y
        self.new_x  = self.register_page.winfo_x() + self.delta_x
        self.new_y = self.register_page.winfo_y() + self.delta_y
        self.register_page.geometry(f"{self.width}x{self.height}+{self.new_x}+{self.new_y}")

    def closing_app(self):
        self.register_page.destroy()

    ## Section for the control definition and placement
    def defining_controls(self):
        import styles
        import colors
        ## Titlebar and control button
        self.title_bar  = tk.Frame(self.register_page , background=colors.login_page_base , height=18)
        self.closing_button  = tk.Button(self.title_bar , text=" X " , command=self.closing_app)
        self.label_image_user  = tk.Label(self.register_page , image=self.user_image)
        ## Section for the username /  password 1 / password 2 / 
        self.username_box  = tk.Entry(self.register_page)
        self.username_line = tk.Frame(self.register_page , height=2 , background=colors.login_page_purple)
        self.password_box  = tk.Entry(self.register_page)
        self.username_check_line  = tk.Frame(self.register_page , height=2 , background=colors.login_page_purple)
        self.password_box_check  = tk.Entry(self.register_page)
        self.password_line  = tk.Frame(self.register_page , height=2 , background=colors.login_page_purple)
        ## Section for the login button / already have an account / Forgot Password
        self.signin_button  = tk.Button(self.register_page , text="Sign In")
        self.alreadyhaveanaccount = tk.Label(self.register_page , text="Already Have an Account ?")
        self.forgot_password   = tk.Label(self.register_page , text="Forgot Password !")
        ## Section for configuring controls 
        self.closing_button.configure(styles.tkinter_styles.button_style_login(self ,self.closing_button))
        self.username_box.configure(styles.tkinter_styles.textbox_configure(self , self.username_box))
        self.password_box.configure(styles.tkinter_styles.textbox_configure(self , self.password_box))
        self.password_box_check.configure(styles.tkinter_styles.textbox_configure(self, self.password_box_check))
        self.signin_button.configure(height=2 , width=10 , justify="center" , relief="sunken",
                                    border=0 , foreground=colors.login_page_base , background=colors.login_button_color , activeforeground=colors.red_color,
                                    activebackground=colors.login_page_purple , font=styles.small_font_bold)
        self.alreadyhaveanaccount.configure(foreground=colors.login_button_color)
        self.forgot_password.configure(foreground=colors.login_button_color)
        ## Inserting the data for the tetxboxes
        self.username_box.insert(0 , "Enter Username")
        self.password_box.insert(0 , "Enter Password")
        self.password_box_check.insert(0 , "Repeat Password")

        ## Section for controls binding
        self.title_bar.bind("<ButtonPress-1>" , self.mouse_click)
        self.title_bar.bind("<B1-Motion>" , self.move_window)
        self.title_bar.bind("<Enter>" , lambda event  : styles.tkinter_styles.change_color_on_hover(self, self.title_bar , colors.login_button_color))
        self.title_bar.bind("<Leave>" , lambda event  :  styles.tkinter_styles.change_color_on_hover(self, self.title_bar , color_name=colors.login_page_base))
        self.alreadyhaveanaccount.bind("<Enter>" , lambda event  :  styles.tkinter_styles.change_foreground_hover(self , self.alreadyhaveanaccount , colors.login_page_purple))
        self.forgot_password.bind("<Enter>" , lambda event : styles.tkinter_styles.change_foreground_hover(self, self.forgot_password , colors.login_page_purple))
        self.alreadyhaveanaccount.bind("<Leave>" , lambda event  :  styles.tkinter_styles.change_foreground_hover(self, self.alreadyhaveanaccount , colors.login_button_color))
        self.forgot_password.bind("<Leave>" , lambda evnet : styles.tkinter_styles.change_foreground_hover(self, self.forgot_password  , colors.login_button_color))
        self.username_box.bind("<FocusIn>" , lambda event : styles.tkinter_styles.textbox_hover(self , self.username_box , self.password_box))
        self.password_box.bind("<FocusIn>" , lambda event :  styles.tkinter_styles.textbox_hover(self , self.password_box , self.password_box))
        self.password_box_check.bind("<FocusIn>" , lambda event : styles.tkinter_styles.textbox_hover(self, self.password_box_check , self.password_box_check))
    def placing_controls(self):
        ## Packing the titlebar 
        self.title_bar.pack(side="top" , fill="x")
        self.closing_button.pack(side="right" , padx=(0 , 0) , fill="x")
        self.label_image_user.pack(side="top" ,pady=(10,10) , fill="x")
        self.username_box.pack(side="top" , padx=(10, 10) , fill="x")
        self.username_line.pack(side="top" , padx=(10,10) , fill="x" , pady=(0,10))
        self.password_box.pack(side="top" , padx=(10,10) , fill="x")
        self.username_check_line.pack(side="top" , padx=(10, 10) , fill="x" , pady=(0 , 10))
        self.password_box_check.pack(side="top" , padx=(10 ,10) , fill="x")
        self.password_line.pack(side="top" , padx=(10,10) , fill="x")
        self.signin_button.pack(side="top" , pady=(10,0) , fill="x" , padx=(10,10))
        self.alreadyhaveanaccount.pack(side="left"  , padx=(10,10))
        self.forgot_password.pack(side="right" , padx=(10,10))

        ## Calling the main app loop
        self.register_page.mainloop()



if __name__ == '__main__':
    register = Register_page(300 , 450)
    register.defining_controls()
    register.placing_controls()
