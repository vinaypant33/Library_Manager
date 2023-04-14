import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pubsub import pub
from datetime import datetime
from dateutil import parser


""" Ui for the dashboard"""
class Userdashboard():
    def __init__(self , received_username , *book_raw_details) -> None:
        # Initial Code for the defining the dashboard
        self.user_dashboard  =Tk()
        self.user_dashboard.title("Library Manager - User")
        self.user_dashboard.geometry("1100x600")
        self.user_dashboard.configure(bg='white')
        self.user_dashboard.iconbitmap(r"Views\app_icon.ico")
        self.user_dashboard.state('zoomed')
        # Received values from the controller via the database or other modules
        self.current_user_username  = received_username
        self.raw_book_details  = book_raw_details
        # Making the values for the book count the book dedtails and the amount incured
        self.book_count = 0
        self.amount_count  = 0
        self.temporary_amount = 0
        # defining the lists here for the user Tabs
        self.all_book_details  = []
        self.all_book_details = book_raw_details
        self.temp_books_to_take = []
        self.available_books_to_take_list  = []
        self.temp_books_taken_by_user = []
        self.book_taken_by_user_list = []
        
        
        self.notification_string  = book_raw_details[2]
        

        # Defining the notificaton images 
        self.notification_open = PhotoImage(file = r"Views\notification_open.png")
        self.notification_none = PhotoImage(file=r"Views\notification_none.png")


        # calling the functions for filling the book details
        self.load_book_details()
    
    # Defining the hover controls
    def return_btn_hover(self , e ):
        self.return_btn.configure(bg='#ededed')
    def return_btn_leave(self,e ):
        self.return_btn.configure(bg='white')
    def options_hover(self , e):
        self.book_taken_options.configure(bg='white') # Check this function 
    def rent_btn_hover(self , e ):
        self.rent_btn.configure(bg='#ededed')
    def rent_btn_leave(self,e ):
        self.rent_btn.configure(bg='white')

    def calculating_amount(self , book_date):
        current_date  = datetime.today().date()
        date2 = book_date
        date2 = parser.parse(date2).date()
        self.date_diff = (current_date - date2).days
        return self.date_diff

    # Defining functions for the controls and for the lists etc
    def load_book_details(self):
        self.temp_books_taken_by_user = self.all_book_details[0]
        self.temp_books_to_take = self.all_book_details[1]
        for book_name in self.temp_books_taken_by_user:
            self.temporary_amount = 0
            self.book_taken_by_user_list.append(book_name[0])
            self.book_count+=1
        for book_name in self.temp_books_to_take:
            self.available_books_to_take_list.append(book_name[0])

    
    # Defining functions for calling the code when the buttons are clicked 
    def renting_book_through_rentbtn(self):
        try:
            # print(self.books_taken_string.get())  This will be sent for the database
            self.book_name_to_rent  = self.books_taken_string.get()
            if self.book_name_to_rent == "Select Book to Rent":
                pass
            else:
                pub.sendMessage("rent_book" , book_details  = self.current_user_username + "," + self.book_name_to_rent)
                self.books_to_take_options['menu'].delete(self.book_name_to_rent)
                self.books_taken_string.set("Select Book to Rent")
                self.available_books_to_take_list.remove(self.book_name_to_rent)
                messagebox.showinfo("Library Manager" , "Added Book : " + self.book_name_to_rent)
        except:
            pass

    def returning_book_through_returnbtn(self):
        selected_item = self.table.selection()[0]
        returned_book_name  = self.table.item(selected_item)['values'][0]
        current_value = self.table .item(selected_item)['values'][4]
        self.amount_count-= current_value
        self.book_count-=1
        # Define the function to add the deleted book into the to take books
        pub.sendMessage("returned_book" , returned_book =  returned_book_name) # Define a function to add the book back again in the database
        self.updating_controls()
        # Define function to delete the options box and add it again in the main screen
        self.available_books_to_take_list.append(returned_book_name)
        self.updating_options_box()
        try:
            messagebox.showinfo("Library Manager" , "Book deleted from the database")
            self.table.delete(self.table.delete(selected_item))
            
        except:
            pass
        
    def adding_current_rendted_book(self, book_name):
        self.book_count+=1
        # Calling updaeting controls for the current update 
        self.amount_count+=12
        self.temporary_amount =12
        self.updating_controls()
        self.table.insert('' ,'end' , text="1" , values=(book_name[0][0]  , book_name[0][1] , book_name[0][2]  , book_name[0][4]  , self.temporary_amount))
        self.amount_incured_label.config(text="Amount Incured || " + str(self.amount_count))

    def notification_button_clicked(self):
        # self.user_dashboard.update()
        x1, y1 = self.notification_button.winfo_rootx(),self.notification_button.winfo_rooty()
        # pub.sendMessage("call_notification", window_axes  = str(x1) +   "," + str(y1))
        if self.notification_string == 'None' or self.notification_string == "" or self.notification_string == ' ':
            pass
        else:
            messagebox.showinfo("Library Manager" , self.notification_string)
            self.notification_string = "None"
            self.notification_button.config(image=self.notification_none)
            pub.sendMessage("button_clicked" , username = self.current_user_username)
        
        
        
    def defining_upper_controls(self):
        # Frames for diff controls
        self.upper_frame = Frame(self.user_dashboard , bg='white')
        self.middle_frame  = Frame(self.user_dashboard , bg='white')
        self.lower_frame  = Frame(self.user_dashboard , bg='white')
        # Label and Buttons etc for the upper controls
        self.username_label = Label(self.upper_frame , text="Welcome || " + self.current_user_username , bg='white')
        if self.notification_string == 'None'or self.notification_string == '' or self.notification_string == ' ':
            print(self.notification_string)
            self.notification_button   = Button(self.upper_frame , image=self.notification_none , width=20 , height=20 , border=0 , bg='white' , command=self.notification_button_clicked)
        # elif len(self.notification_string) > 0:
        #     self.notification_button   = Button(self.upper_frame , image=self.notification_open , width=20 , height=20 , border=0 , bg='white' , command=self.notification_button_clicked)
        else:
            self.notification_button   = Button(self.upper_frame , image=self.notification_none , width=20 , height=20 , border=0 , bg='white' , command=self.notification_button_clicked)
        self.books_taken_label  = Label(self.upper_frame , text="Books Taken || " + str(self.book_count) , bg='white')
        self.amount_incured_label  = Label (self.upper_frame , text="Amount Incured || " + str(self.amount_count) , bg='white')


    def defining_middle_controls_returnbook(self):
        # self.book_to_take_string = StringVar()
        # self.book_to_take_string.set("Select Book to Return")
        # Middle Frame controls
        if  len(self.book_taken_by_user_list) > 0:
            # self.book_taken_options  = OptionMenu(self.middle_frame , self.book_to_take_string , *self.book_taken_by_user_list )
            # self.book_taken_options.configure(bg='white')
            # self.book_taken_options.pack(side='right' , padx=10)
            self.return_btn  = Button(self.middle_frame , text="Return Selected Book" , bg='white' , relief='groove'  , bd=1  ,command=self.returning_book_through_returnbtn)
            self.return_btn.pack(side='right' , padx=15)
            self.return_btn.bind("<Enter>" , self.return_btn_hover)
            self.return_btn.bind("<Leave>" , self.return_btn_leave)
            # self.book_taken_options.bind("<Enter>" , self.options_hover)

    def defining_middle_controls_rentbook(self):
        self.books_taken_string  = StringVar()
        self.books_taken_string.set("Select Book to Rent")
        # Middle frame controls for the book to rent
        if len(self.available_books_to_take_list) > 0:
            self.books_to_take_options  = OptionMenu(self.middle_frame , self.books_taken_string , *self.available_books_to_take_list)
            self.books_to_take_options.configure(bg='white')
            self.books_to_take_options.pack(side='left' , padx=10)
            self.rent_btn = Button(self.middle_frame  ,text="Rent Book" , bg='white' , relief='groove' , bd=1 , command=self.renting_book_through_rentbtn)
            self.rent_btn.pack(side='left' , padx=10)
            self.rent_btn.bind("<Enter>" , self.rent_btn_hover)
            self.rent_btn.bind("<Leave>" , self.rent_btn_leave)


    def defining_lower_controls(self):
        # Treeview defined for the book details
        self.table = ttk.Treeview(self.lower_frame,  columns=("1" , "2" , "3" ,"4" , "5") , show='headings' , height=5)
        self.table.column("# 1" , anchor=CENTER)
        self.table.heading("# 1", text="Book Name")
        self.table.column("# 2", anchor=CENTER)
        self.table.heading("# 2", text="Book Publication")
        self.table.column("# 3", anchor=CENTER)
        self.table.heading("# 3", text="Book Author")
        self.table.column("# 4", anchor=CENTER)
        self.table.heading("# 4", text="Rented Date")
        self.table.column("# 5" , anchor=CENTER)
        self.table.heading("# 5", text="Rent Charged (Rupees)")

    def placing_controls(self):
         # Placing Upper Controls
        self.upper_frame.pack( fill=BOTH , pady=15)
        self.username_label.pack(side='right',padx=15)
        self.notification_button.pack(side='right' , padx=4)
        self.books_taken_label.pack(side='left' , padx=15)
        self.amount_incured_label.pack(side='left' , padx=15)
        # Placing the middle controls
        self.middle_frame.pack(fill=BOTH , pady=10)
        # other options box and some part is already been done  in the if statement 
         # Placing the bottom controls
        self.lower_frame.pack(fill=BOTH , expand=True , side=TOP)
        self.table.pack(fill=BOTH , side=TOP ,expand=True)
        # Calling the main app to run


    # Functions to be called when all the controls are placed
    def filling_treeview(self):
        # self.table.insert('' ,'end' , text="1" , values=(name  , publication , author  , date  , rupees))
        for book_name in self.temp_books_taken_by_user:
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
        self.books_taken_label.config(text="Books Taken || " + str(self.book_count))
        self.amount_incured_label.config(text="Amount Incured || " + str(self.amount_count))

    def updating_options_box(self):
        self.books_to_take_options.destroy()
        self.rent_btn.destroy()
        self.books_to_take_options  = OptionMenu(self.middle_frame , self.books_taken_string , *self.available_books_to_take_list)
        self.books_to_take_options.configure(bg='white')
        self.books_to_take_options.pack(side='left' , padx=10)
        self.rent_btn = Button(self.middle_frame  ,text="Rent Book" , bg='white' , relief='groove' , bd=1 , command=self.renting_book_through_rentbtn)
        self.rent_btn.pack(side='left' , padx=10)
        self.rent_btn.bind("<Enter>" , self.rent_btn_hover)
        self.rent_btn.bind("<Leave>" , self.rent_btn_leave)

    def starting_app(self):
        self.filling_treeview()
        self.user_dashboard.mainloop()


""" Ui for the librarian Dashboard  """
class librariandashboard():

    def __init__(self, username , usernames , available_books ) -> None:
        self.librarian_dashboard = Tk()
        self.librarian_dashboard.title("Library Manager - Librarian")
        self.librarian_dashboard.geometry("1100x600")
        self.librarian_dashboard.configure(bg='white')
        self.librarian_dashboard.iconbitmap(r"Views\app_icon.ico")
        self.available_book_list_fetched  = []
        self.available_books_make = []
        self.available_book_list_fetched = available_books
        self.librarian_dashboard.state('zoomed')
        self.myusername  = username
        # usernames the books and other bookkrelated data will be saved here usign the list 
        self.received_raw_user_details  = usernames
        self.user_details  = [] 
        
        self.setting_user_details()
        
    # place to define the functions to be called for setting the usernames books and other user details
    def setting_user_details(self):
        for names in self.received_raw_user_details:
            self.user_details.append(names[0])
        self.usernames = StringVar()
        self.usernames.set("Choose user :")
        self.getusername_for_contactdetails   = StringVar()
        self.getusername_for_contactdetails.set("Select Username")

        self.message_usernames = StringVar()
        self.message_usernames.set("Select User for notification : ")
        # Setting the book name to be sent to the main book options box
        self.book_data = StringVar()
        self.book_data.set("Choose book to add :")
        for book_name in self.available_book_list_fetched:
            self.available_books_make.append(book_name[0])
            
    def add_book_btn_clicked(self):
        self.chosen_book_name = self.book_data.get()
        self.chosen_user_name  =self.usernames.get()
        # Check the username and the book_name
        if self.chosen_book_name == "Choose book to add :":
            pass
        elif self.chosen_user_name == "Choose user :":
            pass
        else:
            pub.sendMessage("add_book_to_the_user"  , book_and_username = self.chosen_book_name + ","  + self.chosen_user_name)

            messagebox.showinfo("Library Manager" , self.chosen_book_name + " is added to " + self.chosen_user_name)
    
    def defining_upper_controls(self):
         # Frames for diff controls
        self.upper_frame = Frame(self.librarian_dashboard , bg='white')
        self.middle_frame = Frame(self.librarian_dashboard , bg='white')
        self.lowerframe = Frame(self.librarian_dashboard , bg='white')
        self.sendmessageframe = Frame(self.lowerframe, bg='white')
        self.addbooksframe  = Frame(self.librarian_dashboard , bg='white')
        self.getdetailsframe  = Frame(self.librarian_dashboard ,bg='white')
        # Upper Frame Controls : The username  , Books Taken  , Total Amount Incured
        self.username_text   = Label(self.upper_frame ,text="Welcome || " + self.myusername , bg='white')

    # Defining and binding controls for the textboxes and Other Controls
    def messageboxfocus(self , e):
        self.sendmessage.delete(0 , "end")
        self.sendmessage.configure(fg='black')

    def book_name_binding(self, e):
        self.book_name.delete(0 , 'end')
        self.book_name.configure(fg='black')
        
    def book_publication_binding(self,  e):
        self.book_publication.delete(0 , "end")
        self.book_publication.configure(fg='black')
        
    def author_name_binding(self , e):
        self.author_name.delete( 0 , 'end')
        self.author_name.configure(fg='black')
        
    def book_company_binding(self , e):
        self.book_company.delete( 0 , 'end')
        self.book_company.configure(fg='black')


    # Defining functions for different button Clicks 
    def notification_button_click(self):
        self.current_username  = self.message_usernames.get()
        if self.current_username == "Select User for notification :":
            pass
        else:
            pub.sendMessage("notification_alert"  , username_message = self.current_username + "," + self.sendmessage.get())
            messagebox.showinfo("Library Manager" , "Notification sent to : " + self.current_username)
        # pub.sendMessage("user_notification" , )
        self.sendmessage.delete(0 , "end")
        self.sendmessage.insert(0  ,"Enter Notification message for user :")
        self.sendmessage.configure(fg='grey')
        self.librarian_dashboard.focus()
        self.message_usernames.set("Select User for notification :")
    
    """ Function to check the user name and get the details for the overdue books and  total amount incured for the current user """
    def get_user_details(self):
        # print(self.getusername_for_contactdetails.get())
        pub.sendMessage("Done",username = self.getusername_for_contactdetails.get())
        
    def showing_user_details(self , *library_details):
        messagebox.showinfo("I am cliced to show the details")
        print(library_details)
        self.taken_books_list_for_messages = []
        for book_name  in library_details:
            self.taken_books_list_for_messages.append(book_name)
        # messagebox.showinfo("Library Manager" , library_details)
        for book in self.taken_books_list_for_messages:
            print(book)

    def add_book_todatabaseclick(self):
        # Getting the book details and sharing the same 
        pub.sendMessage("book_details_Save" ,book_data = self.book_name.get() + "," + self.book_publication.get() + "," +  self.author_name.get()  + "," + self.book_company.get())
        self.book_name.delete( 0 , 'end')
        self.book_name.insert(0 , "Enter Book Name")
        self.book_name.configure(fg='grey')
        self.book_publication.delete( 0 ,'end')
        self.book_publication.insert(0 , "Enter Publication Name")
        self.book_publication.configure(fg='grey')
        self.author_name.delete( 0 ,'end')
        self.author_name.insert(0  , "Enter Book Author Name")
        self.author_name.configure(fg='grey')
        self.book_company.delete(0 , 'end')
        self.book_company.insert(0 , "Enter Book Company")
        self.book_company.configure(fg='grey')
        self.librarian_dashboard.focus()
        
    
    
    def defining_middle_controls(self):
        # Middle Frame Controls 
        self.numberofusers = Frame(self.middle_frame , height=100 , width=100   , padx=40, pady=20)
        self.users_text = Label(self.numberofusers , text="Total Users | 9")
        self.numberofbooks = Frame(self.middle_frame , height=100  , padx=40 , pady=20)
        # self.books_count  =Label(self.numberofbooks , height=20 , bg='blue' , padx=20 , pady=20)
        self.books_count  =Label(self.numberofbooks , text="Total Books | 22")
        self.borrowedbooks  =Frame(self.middle_frame , height=100 , padx=40 , pady=20)
        self.borrowedbooks_count  = Label(self.borrowedbooks , text="Borrowed Books | 16")
        self.overduebooks = Frame(self.middle_frame , height=100,  padx=40 , pady=20)
        self.overduebooks_count = Label(self.overduebooks , text="Overdue Books | 6")
        self.total_amount = Frame(self.middle_frame , height=100 , width=100  , padx=40 , pady=20)
        self.amount_incured = Label(self.total_amount , text="Amount Incured | 350")
        
        # Controls to add the book to any user
        self.available_books_list  = OptionMenu(self.lowerframe , self.book_data , *self.available_books_make)
        self.setbook = Button(self.lowerframe ,text="Add Book to User" , command =self.add_book_btn_clicked )
        self.usernames_option = OptionMenu(self.lowerframe , self.usernames , *self.user_details )

        # second user select for the returning book : 
        self.return_book_data =StringVar()
        self.return_book_data.set("Choose book to return")
        self.return_books = ["asdf" , "asdfasdf" , "dasfafasdf", "4563456"]
        # self.return_books_list = OptionMenu(self.lowerframe , self.return_book_data , *self.return_books)
        # self.returnbook_btn = Button(self.lowerframe , text="Return Selected Book")

        # Controls to send message to the user 
        self.sendmessage  =Entry(self.sendmessageframe , fg='gray' , width=50)
        self.sendmessage.insert(0 , "Enter Notification message for user :")
        self.sendmessage.bind("<FocusIn>" , self.messageboxfocus)

       

        self.username_for_message = OptionMenu(self.lowerframe , self.message_usernames , *self.user_details )
        self.sendmessagebtn = Button(self.lowerframe , text="Send Notification" , command=self.notification_button_click)

    def defining_lower_controls(self):
        # Defining controls for adding the books in the database
        self.book_name= Entry(self.addbooksframe , fg='grey' , width=30)
        self.book_name.insert( 0 , "Enter Book Name")
        self.book_company  = Entry(self.addbooksframe, fg='grey' , width=30)
        self.book_company.insert( 0 , "Enter Book Company")
        self.book_publication = Entry(self.addbooksframe ,fg='grey' , width=30)
        self.book_publication.insert(0  ,"Enter Publication Name")
        self.author_name  =Entry(self.addbooksframe ,fg='grey' , width=30)
        self.author_name.insert( 0 , "Enter Book Author Name")
        
        
        self.add_book = Button(self.addbooksframe , text="Add Book to the database" , command=self.add_book_todatabaseclick)
        
        # Setting the focus in Controls 
        self.book_name.bind("<FocusIn>" , self.book_name_binding)
        self.book_company.bind("<FocusIn>" , self.book_company_binding)
        self.book_publication.bind("<FocusIn>" ,self.book_publication_binding )
        self.author_name.bind("<FocusIn>" , self.author_name_binding)
        
        
        # Define contrls to get the username and get the contact controls 
        """ Here also the username will be contrlled using the function and only stringvar will be here"""
      
        self.username_for_contact = OptionMenu(self.getdetailsframe , self.getusername_for_contactdetails , *self.user_details)
        self.usernamegetbtn = Button(self.getdetailsframe , text="Get User Details" , command=self.get_user_details)
        
  
    
    def placing_controls(self):
        # Placing the upper controls
        self.upper_frame.pack(fill=BOTH , pady=5)
        self.middle_frame.pack(fill=BOTH, pady=5)
        self.lowerframe.pack(fill=BOTH ,pady=5)
        self.sendmessageframe.pack(fill=BOTH ,  side='right', padx=5)
        self.username_text.pack(side='right' , padx=10)

        # Placing the middle controls
        self.numberofusers.pack(side='left' , padx=10)
        self.users_text.pack(side='left' , padx=10)
        self.numberofbooks.pack(side='left' , padx=10)
        self.books_count.pack(side='left' , padx=10)
        self.borrowedbooks.pack(side='left' , padx=10)
        self.borrowedbooks_count.pack(side='left'  ,padx=10)
        self.overduebooks.pack(side='left' , padx=10)
        self.overduebooks_count.pack(side='left' , padx=10)
        self.total_amount.pack(side='right' , padx=20)
        self.amount_incured.pack(side='right' , padx=20)
        self.available_books_list.pack(side='left' , padx=10)
        self.usernames_option.pack(side='left' , padx=10)
        self.setbook.pack(side='left' , padx=10)

        # placing control for return book data 
        # self.return_books_list.pack(side='left' , padx=5)
        # self.returnbook_btn.pack(side='left' , padx=5)

        # Placing send message frames
        self.sendmessagebtn.pack(side='right' ,pady =2 ,padx=2)
        self.username_for_message.pack(side='right' , pady=2 , padx=2)
        self.sendmessage.pack(pady=5)

        #placing the add books controls
        self.addbooksframe.pack(fill=BOTH)
        self.book_name.pack(side='left' , padx=10)
        self.book_company.pack(side='left'  ,padx=10)
        self.book_publication.pack(side='left'  ,padx=10)
        self.author_name.pack(side='left' , padx=10)
        self.add_book.pack(side='left' , padx=10)
        
        # Setting controls for the getting the user details
        self.getdetailsframe.pack(fill=BOTH , pady=20)
        self.username_for_contact.pack(side='left' , padx=10)
        self.usernamegetbtn.pack(side='left' , padx=10)
        
        # Calling the main app
        self.librarian_dashboard.mainloop()
