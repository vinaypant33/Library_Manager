import tkinter as tk 
from tkinter import messagebox
from pubsub import pub
from PIL import Image , ImageTk
from tkinter import ttk  
import customtkinter as ctk
import styles 
import colors
from datetime import datetime
from dateutil import parser

class Dashboard():

    def __init__(self , width  , height , user_details  , book_to_take) -> None:
        
     
        self.dashboard  = tk.Tk()
        self.height  = height 
        self.width  = width 
        self.screen_width  = self.dashboard.winfo_screenwidth()
        self.screen_height   = self.dashboard.winfo_screenheight()
        self.x_coordinate  = (self.screen_width //2 )  - (self.width // 2)
        self.y_coordinate   = (self.screen_height // 2) - (self.height // 2)
        self.dashboard.geometry(f'{self.width}x{self.height}+{self.x_coordinate}+{self.y_coordinate}')
        self.dashboard.overrideredirect(1)
        self.dashboard.configure(background=colors.white_color)
        ## user Details and books list to take will be segrated here : user details contains number of users and their details
        self.number_of_users  = 0
        self.user_details  = user_details
        self.books_to_take  = book_to_take


        ## Operating the data on user details and books to take 
        for user in self.user_details:
            self.number_of_users+=1


        
    ## List for the  available for the available books and the current users
        self.available_books = []
        self.current_users  = []
        self.current_users_2 = []

    ## Adding the dummy data for the books which will be replaed by the database later 
        self.available_books.append("Dummy Book -1 ")
        self.available_books.append("Dummy Book -2")
        self.available_books.append("Dummy Books - 3")
        self.current_users.append("Dummy User -1 ")
        self.current_users.append('Dummy User -2')
        self.current_users.append('Dummy User -3')
        self.current_users_2.append("User Dummy -1")
        self.current_users_2.append("User Dummy -2")
        self.current_users_2.append('User Dummy -3')


    ## defining the stringvar for the opetion menu or the combobox or the  bootstrap combobox 
        self.cb  = tk.StringVar()
        self.cb.set("Choose Book")
        self.cu = tk.StringVar()
        self.cu.set("Choose User")
        self.cu2 = tk.StringVar()
        self.cu2.set("Choose User")

    ## Defining functions for the control  : 
    def closing_app(self):
        self.dashboard.destroy()
    
    def mouse_click(self , event):
        self.x  = event.x
        self.y = event.y
    
    def move_window(self , event):
        self.delta_x = event.x - self.x
        self.delta_y =  event.y  - self.y
        self.new_x = self.dashboard.winfo_x() + self.delta_x
        self.new_y  = self.dashboard.winfo_y() + self.delta_y
        self.dashboard.geometry(f"{self.width}x{self.height}+{self.new_x}+{self.new_y}")



    def defining_controls(self):
        import colors
        import styles
        self.titlebar  = tk.Frame(self.dashboard)
        self.titlebar.pack_propagate(1)
        self.close_btn   = tk.Button(self.titlebar , text=" X " , command=self.closing_app)
        # Frames for containing the controls :  Upper Middle and Lower 
        self.upper_frame  = tk.Frame(self.dashboard)
        self.middle_frame  = tk.Frame(self.dashboard)
        # self.lower_frame  = tk.Frame(self.dashboard)
        ## Frames for the upper side controls
        self.users_frame   = tk.Frame(self.upper_frame)
        self.books_frame = tk.Frame(self.upper_frame)
        self.borrowed_books_frame  = tk.Frame(self.upper_frame)
        self.overdue_books_frame = tk.Frame(self.upper_frame)
        self.amount_incured_frame  = tk.Frame(self.upper_frame)
        ## Controls for the upper control : Labels
        ## Small font labels 
        self.total_users_text  = tk.Label(self.users_frame , text="Total Users" , background=colors.white_color , font=styles.super_small_font_bold , foreground=colors.login_button_color)
        self.total_users  = tk.Label(self.users_frame , text=self.number_of_users , font=styles.largest_font_bold , background=colors.white_color , foreground=colors.login_page_purple)
        self.total_books_text = tk.Label(self.books_frame , text="Total Books" , background=colors.white_color , font=styles.super_small_font_bold , foreground=colors.login_button_color)
        self.total_books  = tk.Label(self.books_frame , text="0" , font=styles.large_font_bold  , background=colors.white_color , foreground=colors.login_page_purple)
        self.borrowed_books_text = tk.Label(self.borrowed_books_frame , text="Borrowed Books" , background=colors.white_color , font=styles.super_small_font_bold , foreground=colors.login_button_color)
        self.borrowed_books = tk.Label(self.borrowed_books_frame , text="0" ,font=styles.large_font_bold , background=colors.white_color , foreground=colors.login_page_purple)
        self.overdue_books_text  = tk.Label(self.overdue_books_frame , text="Overdue Books" , background=colors.white_color , font=styles.super_small_font_bold , foreground=colors.login_button_color)
        self.overdue_books = tk.Label(self.overdue_books_frame , text="0" , font=styles.large_font_bold , background=colors.white_color , foreground=colors.login_page_purple)
        self.amount_incured_text  =tk.Label(self.amount_incured_frame , text="Amount Incured" , background=colors.white_color ,font=styles.super_small_font_bold , foreground=colors.login_button_color )
        self.amount_incured = tk.Label(self.amount_incured_frame , text="0" , font=styles.large_font_bold , background=colors.white_color , foreground=colors.login_page_purple)
        ## Middle Controls  Example fo the ttk combobox 
        self.choose_book_combobox = ctk.CTkComboBox(self.middle_frame , values=self.available_books , variable=self.cb)
        self.choose_user_combobox  = ctk.CTkComboBox(self.middle_frame , values=self.current_users , variable=self.cu)
        self.add_book_btn  = tk.Button(self.middle_frame , text='Add Book to User')
        ## Entry Boxes for the Middle Frame 
        self.book_name_box   = ctk.CTkEntry(self.middle_frame)
        self.book_company_box  = ctk.CTkEntry(self.middle_frame)
        self.publication_name_box  = ctk.CTkEntry(self.middle_frame)
        self.book_author_box   = ctk.CTkEntry(self.middle_frame)
        self.add_book_to_database = tk.Button(self.middle_frame , text="Add Book to Database")
        self.get_user_details  = ctk.CTkComboBox(self.middle_frame , values=self.current_users_2 , variable=self.cu2)
        self.get_user_details_btn  = tk.Button(self.middle_frame  , text="Get User Details")
        self.send_notification_btn = tk.Button(self.middle_frame , text="Send Notification")
        self.message_box  = ctk.CTkEntry(self.middle_frame , placeholder_text="Enter Message to Send" , width=300 , corner_radius= 0  ,height=30)

    
    ## Configuring the contols : 
        self.titlebar.configure(height=20 , background=colors.login_page_purple)
        self.close_btn.configure(styles.tkinter_dashboard_styles.button_style_login(self, self.close_btn))
    
        ## Configuring the frames for the dummy background 
        # self.upper_frame.configure(background=colors.black_color ,  height=290 , width=228)
        self.middle_frame.configure(background = colors.white_color ,height=290 , width=228)
        # self.lower_frame.configure(background=colors.grey_text_color , height=290 , width=228)

        self.users_frame.configure(background=colors.white_color , height=200 , width=228)
        self.books_frame.configure(background=colors.white_color , height=200 , width=228)
        self.borrowed_books_frame.configure(background=colors.white_color , height=200 , width=228)
        self.overdue_books_frame.configure(background=colors.white_color, height=200 , width=228)
        self.amount_incured_frame.configure(background=colors.white_color, height=200 , width =228)

        ## Textbox configuring : 
        self.book_name_box.configure(width = 300 ,height = 30 , corner_radius = 0  , placeholder_text = "Book Name")
        self.book_company_box.configure(width = 300 ,height = 30 , corner_radius = 0  , placeholder_text = "Book Company Name")
        self.publication_name_box.configure(width = 300 ,height = 30 , corner_radius = 0  , placeholder_text = "Publication Name")
        self.book_author_box.configure(width = 300 ,height = 30 , corner_radius = 0  , placeholder_text = "Book Author Name")
        ## Configuring the books and the users 
        self.choose_book_combobox.configure(styles.tkinter_dashboard_styles.combobox_style(self , self.choose_book_combobox))
        self.choose_user_combobox.configure(styles.tkinter_dashboard_styles.combobox_style(self , self.choose_user_combobox))
        self.add_book_btn.configure(styles.tkinter_dashboard_styles.button_style(self , self.add_book_btn , colors.login_page_purple , colors.white_color , 25 , 2))
        self.add_book_to_database.configure(styles.tkinter_dashboard_styles.button_style(self , self.add_book_to_database , colors.login_page_purple , colors.white_color , 37 , 2))
        self.get_user_details.configure(styles.tkinter_dashboard_styles.combobox_style(self , self.get_user_details))
        self.get_user_details_btn.configure(styles.tkinter_dashboard_styles.button_style(self , self.get_user_details_btn , colors.login_page_purple  , colors.white_color , 25,2))
        self.send_notification_btn.configure(styles.tkinter_dashboard_styles.button_style(self , self.send_notification_btn , colors.login_page_purple , colors.white_color  , 37 , 2))
    ## Binding the controls : 
        self.titlebar.bind("<ButtonPress-1>"  ,self.mouse_click)
        self.titlebar.bind("<B1-Motion>" , self.move_window)

    

    def placing_controls(self):
        ## Placing the frames and the Labels for all the controls
        self.titlebar.pack(side="top" , fill="x")
        self.close_btn.pack(side="right" , padx=(0 , 0))
        ## Packing the frames
        self.upper_frame.pack(side="top" , pady=(5 ,5) , padx=(10 ,10) , fill="x")
        self.middle_frame.pack(side="top" , pady=(5 ,5 ) , padx=(10,10) , fill="x")
        # self.lower_frame.pack(side="top" , pady=(5 , 5) , padx=(10,10) , fill="x")
        ## calling the main app
        ## Placing the frames for the words
        self.users_frame.pack(side="left" , pady=(5,5) , padx=(10 , 5))
        self.books_frame.pack(side="left" ,pady=(5,5) , padx=(5 , 5))
        self.borrowed_books_frame.pack(side="left" , pady=(5,5) , padx=(5, 5))
        self.overdue_books_frame.pack(side="left" , pady=(5,5) ,padx=(5,5))
        self.amount_incured_frame.pack(side="left" , pady=(5,5) , padx=(5,5))
        ## Placing the labels and and setting them in the Frames 
        self.total_users_text.place(x = 10 , y= 10)
        self.total_users.place(relx=0.5 , rely=0.5  , anchor="center")
        self.total_books_text.place(x=10 , y=10)
        self.total_books.place(relx=0.5 , rely=0.5 , anchor="center")
        self.borrowed_books_text.place(x = 10 , y =10)
        self.borrowed_books.place(relx=0.5 , rely=0.5 , anchor="center")
        self.overdue_books_text.place(x = 10 , y= 10)
        self.overdue_books.place(relx=0.5 , rely=0.5 , anchor="center")
        self.amount_incured_text.place(x =10 , y=10)
        self.amount_incured.place(relx=0.5 , rely=0.5 , anchor="center")
        ## Placing the middle controls : 
        self.choose_book_combobox.place(x=10 , y =10)
        self.choose_user_combobox.place(x = 10 , rely   = 0.2)
        self.add_book_btn.place( x = 10 , rely= 0.4)
        self.book_name_box.place(x  =250 , y  =10)
        self.book_company_box.place(x = 250 , rely  = 0.2)
        self.publication_name_box.place(x  =250 , rely = 0.4)
        self.book_author_box.place(x = 250 , rely= 0.6)
        self.add_book_to_database.place(x  =250  , rely=0.8)

        self.get_user_details.place(x = 600 , y = 10)
        self.message_box.place(x = 600 , rely = 0.2)
        self.send_notification_btn.place(x = 600 , rely = 0.4)
        self.get_user_details_btn.place(x = 950 , y = 10)
    ## Running the main application
        self.dashboard.mainloop()



''' User Dashboard Ui Tkitner '''
class User_Dashboard():
    def __init__(self , width , height , username , taken_books , available_books,  notification_string) -> None:
        

        self.user_dashboard = tk.Tk()
        self.width  = width
        self.height  = height
        self.screen_width  = self.user_dashboard.winfo_screenwidth()
        self.screen_height  = self.user_dashboard.winfo_screenheight()
        self.x_coordinate  = (self.screen_width // 2) - (self.width // 2)
        self.y_coordinate   = (self.screen_height // 2) - (self.height // 2)
        self.user_dashboard.geometry(f'{self.width}x{self.height}+{self.x_coordinate}+{self.y_coordinate}')
        self.user_dashboard.overrideredirect(1)


        ## Processing the details received from the controller : 
        self.temporary_amount  = 0
        self.amount_count  =  0
        self.book_count  = 0
        ## Setting the current choise for the combobox
        self.current_choice = 'none'
        self.username = username
        self.taken_books_user  = []
        self.available_books_user  = []
        self.taken_books_table  = []
        self.taken_books_table = taken_books
        self.notification_string  = notification_string
        # Filling the available books string
        self.taken_books_user.clear()
        for book in taken_books:
            self.taken_books_user.append(book[0])

        self.available_books_user.clear()
        for available_book in available_books:
            self.available_books_user.append(available_book[0])

        ## Importing the image and resizign the same for the notification part 
        open_notification  = Image.open(r'Assets\bell-alarm.png')
        resized_notification  = open_notification.resize((20,20))
        self.open_notification = ImageTk.PhotoImage(resized_notification)
        closed_notification = Image.open(r'Assets\bell.png')
        resized_closed_notification = closed_notification.resize((20,20))
        self.closed_notification = ImageTk.PhotoImage(resized_closed_notification)

        ## Setting the list for the available books 
        self.availabele_books  = []
        self.taken_books  = []


        # Setting up the stringvar :
        self.cb = tk.StringVar()
        self.cb.set("Available Books")


    
## Funnctions for the basic working of the app
    def mouse_click(self  , event):
        self.x = event.x
        self.y = event.y  
    
    def move_window(self , event):
        self.deltax = event.x - self.x
        self.deltay = event.y  - self.y
        self.newx = self.user_dashboard.winfo_x() + self.deltax
        self.newy = self.user_dashboard.winfo_y() + self.deltay
        self.user_dashboard.geometry(f'{self.width}x{self.height}+{self.newx}+{self.newy}')
    
    def closing_app(self):
        self.user_dashboard.destroy()

    def setting_current_value(self , choice):
        # global current_choice  # Make the current choice global to access later
        self.current_choice  = choice ## Sets the current value which will be used to delete th list later
        # self.returning_book()

    ## Change the code from here and make the code change : for deleting the books and treeview and clear treeview and combobox
    def renting_book(self):
        for item in self.table.get_children():
            self.table.delete(item)
        # deleting the item from the list and call the function for the filling table and make the combobox again.  
        self.available_books_user.remove(self.current_choice)
        self.books_combobox.destroy()
        # Make new combobox and pack the item again in the Frame with the new listbox 
        self.updating_options_box()
        self.filling_treeview()
        # Sending the messagebox to rent the book to the current user 
        pub.sendMessage('add_book' , book_details  = self.username + ',' + self.current_choice)

    def returning_book(self):
        selected_item = self.table.selection()[0]
        returned_book_name  = self.table.item(selected_item)['values'][0]
        current_value = self.table .item(selected_item)['values'][4]
        self.amount_count-= current_value
        self.book_count-=1
        self.updating_controls()
        pub.sendMessage("returned_book" , returned_book =  returned_book_name) # Define a function to add the book back again in the database
        self.available_books_user.append(returned_book_name)
        self.updating_options_box()
        try:
            messagebox.showinfo("Library Manager" , "Deleting book from a database")
            self.table.delete(self.table.delete(selected_item))
        except:
            pass


    def updating_options_box(self):
        self.books_combobox.destroy()
        ## For now copying the code from the above function later will convert the common code to the seperate function : 
        self.books_combobox  = ctk.CTkComboBox(self.middle_frame , values=self.available_books_user, variable=self.cb , command=self.setting_current_value)
        self.books_combobox.configure(button_color = colors.login_page_purple , border_color = colors.black_color , width = 200 , button_hover_color = colors.red_color , fg_color = colors.white_color , corner_radius  = 0,
                                      border_width = 1 , dropdown_fg_color = colors.white_color) ## Command will be used to call the callback function
        self.books_combobox.configure(variable  = self.cb)
        self.books_combobox.set('')
        self.books_combobox.set('Available Books')
        ## Now Packing the combobox into the middle frame
        self.books_combobox.place(x =130 , y =10)

    ## Change the code from here too and make the change in combbobox and delete the controls
    def defining_controls(self):
        ## Titlebar and  the closign button
        self.titlebar  = tk.Frame(self.user_dashboard , height=20 , background=colors.login_page_purple)
        self.titlebar.pack_propagate(1)
        self.closing_button  = tk.Button(self.titlebar , text=' X ' , command=self.closing_app)
        # Frame for the 3 Frames parts equal Each and  had to be inside one frame stretched end to end 
        self.upper_frame  = tk.Frame(self.user_dashboard)
        self.upper_frame.pack_propagate(0)
        self.upper_frame_shadow  = tk.Frame(self.user_dashboard)
        # Controls for the upper frame 
        self.books_taken_text  =tk.Label(self.upper_frame , text="Books Taken ||" , font=styles.small_font_bold , background=colors.white_color)
        self.total_Balance_text  =tk.Label(self.upper_frame , text="Total Amount ||" ,font=styles.small_font_bold , background=colors.white_color)
        self.notification_icon = tk.Label(self.upper_frame , image=self.closed_notification , background=colors.white_color)
        self.user_name  = tk.Label(self.upper_frame ,text="Welcome || " + self.username , font=styles.small_font_bold , background=colors.white_color)
        # Second Frame for the Books to rent add books and return books button 
        self.middle_frame  = tk.Frame(self.user_dashboard , height=50 , background=colors.white_color)
        self.middle_frame.pack_propagate(0)
        self.middle_frame_shadow = tk.Frame(self.user_dashboard  ,height=2 , background=colors.grey_text_color)
        # Buttons and remaining other controls 
        self.rent_book_button   = tk.Button(self.middle_frame , text="Rent Selected Book" , command=self.renting_book)
        self.books_combobox  = ctk.CTkComboBox(self.middle_frame , values=self.available_books_user, variable=self.cb , command=self.setting_current_value)
        self.return_book_button = tk.Button(self.middle_frame , text="Return Selected Book", command=self.returning_book )
        # Frame for the table and in which the table will reside with the books names and other data 
        self.table = ttk.Treeview(self.user_dashboard , columns=("1" , "2" , "3" ,"4" , "5") , show='headings' , height=5)
        # Sstting the column names and headings for the columns 
        self.table.column("#1" , anchor='center')
        self.table.heading("#1" ,  text="Book Name")
        self.table.column("# 2", anchor='center')
        self.table.heading("# 2", text="Book Publication")
        self.table.column("# 3", anchor='center')
        self.table.heading("# 3", text="Book Author")
        self.table.column("# 4", anchor='center')
        self.table.heading("# 4", text="Rented Date")
        self.table.column("# 5" , anchor='center')
        self.table.heading("# 5", text="Rent Charged (Rupees)")

    ## Configuring the controls : 
        self.closing_button.configure(styles.tkinter_dashboard_styles.button_style_login(self , self.closing_button))
        self.upper_frame.configure(background=colors.white_color , height=50)
        self.upper_frame_shadow.configure(background=colors.grey_text_color , height=2)
        self.rent_book_button.configure(styles.tkinter_dashboard_styles.dashboard_button_style(self , self.rent_book_button , colors.login_page_purple , colors.white_color , colors.red_color , colors.black_color))
        self.books_combobox.configure(button_color = colors.login_page_purple , border_color = colors.black_color , width = 200 , button_hover_color = colors.red_color , fg_color = colors.white_color , corner_radius  = 0,
                                      border_width = 1 , dropdown_fg_color = colors.white_color) ## Command will be used to call the callback function
        self.return_book_button.configure(styles.tkinter_dashboard_styles.dashboard_button_style(self , self.return_book_button , colors.login_page_purple , colors.white_color , colors.red_color , colors.black_color))
        self.table.configure(height=100)

    ## Binding the controls
        self.titlebar.bind("<ButtonPress-1>" , self.mouse_click)    
        self.titlebar.bind("<B1-Motion>" , self.move_window)

    def calculating_amount(self , book_date):
            current_date  = datetime.today().date()
            date2 = book_date
            date2 = parser.parse(date2).date()
            self.date_diff = (current_date - date2).days
            return self.date_diff
    ## Function to fill the treeview
    def filling_treeview(self):
            # CLearing the treeview 
            for item in self.table.get_children():
                self.table.delete(item)
            self.book_count  = 0
            self.amount_count = 0
            # self.table.insert('' ,'end' , text="1" , values=(name  , publication , author  , date  , rupees))
            for book_name in self.taken_books_table:
                self.book_count+=1
                self.date_difference = self.calculating_amount(book_name[4])
                self.date_difference = int(self.date_difference)
                if self.date_difference == 0:
                    self.temporary_amount = 12
                    self.amount_count+=12
                elif  7 > self.date_difference > 0 :
                    self.temporary_amount  = 12 * self.date_difference
                    self.amount_count+= self.temporary_amount
                else:
                    # self.date_difference  > 12
                    self.temporary_amount = 12 * self.date_difference + 100
                    self.amount_count+= self.temporary_amount
                
                self.table.insert('' ,'end' , text="1" , values=(book_name[0]  , book_name[1] , book_name[2]  , book_name[4]  , self.temporary_amount))
                self.updating_controls()


    def updating_controls(self):
            self.books_taken_text.config(text="Books Taken || " + str(self.book_count))
            self.total_Balance_text.config(text="Amount Incured || " + str(self.amount_count))


## Placing the controls
    def placing_controls(self):
        self.titlebar.pack(side="top" , fill="x")
        self.closing_button.pack(side="right" , padx=(0 , 0))
        self.upper_frame.pack(side="top" , fill="x")
        self.upper_frame_shadow.pack(side="top" , fill="x")
        self.books_taken_text.pack(side="left" , padx=(10,0))
        self.total_Balance_text.pack(side="left" , padx=(10,0))
        self.user_name.pack(side="right" , padx=(10,10))
        self.notification_icon.pack(side="right"  , padx=(10,10))
        self.middle_frame.pack(side="top" , pady=(0 ,0) ,fill="x")
        self.middle_frame_shadow.pack(side="top" , pady=(0,0) , fill="x")
        self.rent_book_button.pack(side="left" , padx=(10,0))
        self.books_combobox.place(x =130 , y =10)
        self.return_book_button.pack(side="right" , padx=(10,10))
        self.table.pack(fill='both')
        ## Filling the data in the app controls before calling the main loop  : 
        self.filling_treeview()
        # Calling the main app : 
        self.user_dashboard.mainloop()
                

if __name__ == '__main__':
    # db  = Dashboard(1200,500)
    # db.defining_controls()
    # db.placing_controls()
    udb = User_Dashboard(1000 , 500 , "vinay Pant")
    udb.defining_controls()
    udb.placing_controls()
