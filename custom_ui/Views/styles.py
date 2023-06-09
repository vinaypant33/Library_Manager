import tkinter as tk
from tkinter import messagebox
from PIL import Image ,ImageTk






## Setting font sizes 
medium_font  = ('Arial', 18)
small_font_bold  = ('Arial', 11 , 'bold')
small_font  = ('Arial' , 10)
super_small_font  = ('Arial' , 8)
large_font_bold = ('Arial' , 28 , 'bold')
super_small_font_bold = ('Arial' , 10 , 'bold')

## Defining class for the styles
class tkinter_styles():

    def __init__(self) -> None:
        pass

    def button_style_login(self, button):
        import colors
        button.configure(background=colors.login_button_color , foreground=colors.login_page_base , bd= 0 , 
                         activeforeground=colors.black_color , activebackground=colors.red_color)

    def textbox_configure(self, textbox):
        import colors
        textbox.configure(background=colors.login_page_base, border=0 , font=medium_font , bd = 0  , relief="flat" , 
                                    justify="center" , foreground = colors.grey_text_color )

    def textbox_hover(self, textbox , matching_control):
        import colors
        textbox.configure(foreground = colors.black_color)
        ## time.sleep(1)
        textbox.delete(0 , 'end')
        if textbox == matching_control:
            matching_control.configure(show="*")
    
    def login_line_configure(self , login_line):
        import colors
        login_line.configure(height=3 , background = colors.login_page_purple)
    
    def change_color_on_hover(self, controlname , color_name):
        controlname.configure(background=color_name)

    def change_foreground_hover(self , controlname ,  colorname):
        controlname.configure(foreground = colorname)


class tkinter_dashboard_styles(tkinter_styles):

    def __init__(self) -> None:
        super().__init__()

    def combobox_style(self , combobox ):
        import colors
        combobox.configure(corner_radius = 0  , button_color = colors.white_color , border_color = colors.white_color  , button_hover_color = colors.login_page_base,
                                            width = 205)

    def button_style(self, button , color  , fg_color, width , height):
        import colors
        button.configure(background = color , foreground = fg_color , width = width , height = height , font = small_font , relief = 'flat' , justify = 'center' , bd= 0,
                         activebackground  = colors.login_button_color , activeforeground  = colors.black_color)
    
    def dashboard_button_style(self , button , bg_color , fg_color , active_bg , active_fg ):
        import colors
        button.configure(background = bg_color , foreground = fg_color  , activebackground = active_bg , activeforeground =active_fg  , bd= 0 , relief = 'flat')