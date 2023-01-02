import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pubsub import pub


""" UI for the user dashboard"""
class Userdashboard(): 
    def __init__(self , received_username , *initial_book_details) -> None:
        # Intital code for the dashboard and Size
        self.user_dashboard = Tk()
        self.user_dashboard.title("Library Manager - User")
        self.user_dashboard.geometry("1100x600")
        self.user_dashboard.configure(bg='white')
        self.user_dashboard.iconbitmap(r"Views\app_icon.ico")
        
        # Received values from the database would be defined here and  should be plcaed via a function
        self.current_username  = received_username
        self.book_details = initial_book_details
        self.book_count  = 0
        
        # Variables for the book_details and to be stored in the treeview
        self.all_book_details  = []
        self.all_book_details = initial_book_details
        self.user_taken_books  = []
        self.user_taken_books = self.all_book_details[0]
        self.books_to_take = []
        self.books_to_take  = self.all_book_details[1]
        self.options_book_name  = []
        self.options_book_return = []
        self.per_book_pricing  = []

        """ Checking here if any of the list have 0 elements then adding a null value just for the sake of controls"""
        # if len(self.user_taken_books) > 0 :
        #     pass
        # else:
        #     self.user_taken_books.append("Null")
        # if len(self.books_to_take) > 0:
        #     pass
        # else:
        #     self.books_to_take.append("Null")
        
        
        # Calling function to set and receive the book details and set the treeview
        self.sort_book_details()
        
        # Defining the images for the application ( None and received notification )
        self.notification_open = PhotoImage(file = r"Views\notification_open.png")
        self.notification_none = PhotoImage(file=r"Views\notification_none.png")
        
        
        # Calling the functions for defining the controls and placing them
        # self.defining_controls()
        # self.defining_middle_controls()
        # self.defining_bottom_controls()
        # self.placing_controls()

    # Defining function to be called for the  controls to show data  
    def sort_book_details(self):
        # Setting the string for the 
        self.books_that_returned_string  = StringVar()
        self.books_that_returned_string.set("Choose Book to Return")
    
        self.books_to_rent_string= StringVar()
        self.books_to_rent_string.set("Choose Book to Rent")

        # Try to make the book options for setting the books name for the options box
        try: 
            for book_name in self.user_taken_books:
                self.options_book_name.append(book_name[0])
        except:
            print("Error occured in the book options book")
        try:
            for book_name in self.books_to_take:
                self.options_book_return.append(book_name[0])
        except Exception as e :
            print("Error for book return  " + str(e))
            

    # Defining functions : for Hover ( diff controls )
    def rent_btn_hover(self , e ):
        self.rentbtn.configure(bg='#ededed')
    def rent_btn_leave(self,e ):
        self.rentbtn.configure(bg='white')
    def return_btn_hover(self ,e):
        self.returnbtn.configure(bg='#ededed')
    def return_btn_leave(self , e):
        self.returnbtn.configure(bg='white')
    def options_hover(self , e):
        self.books_taken_options.configure(bg='white')


    ## Defining function for the button click and other actions
    def delete_icon(self):
        self.notification_btn.destroy()
    
    def current_message(self , notification_string):
        messagebox.showinfo("Library Manager" , notification_string)


    # Defining the upper controls ( upper layer controls )
    def defining_controls(self):
        # Frames for diff controls
        self.upper_frame = Frame(self.user_dashboard , bg='white')
        self.middle_frame = Frame(self.user_dashboard , bg='white')
        self.lowerframe = Frame(self.user_dashboard , bg='white')
        # Upper Frame Controls : The username  , Books Taken  , Total Amount Incured
        self.username_text   = Label(self.upper_frame ,text="Welcome || " + self.current_username, bg='white')
        # self.notification_btn  = Button(self.upper_frame ,)
        # self.name_btn = Label(self.upper_frame , image=self.notification_closed)
        self.notification_btn = Button(self.upper_frame , image=self.notification_none, width=20 , height=20 , border=0  , bg='white' )
        self.books_taken   = Label(self.upper_frame, text="Books Taken  || " + str(self.book_count) , bg='white')
        self.amount_incured  = Label(self.upper_frame , text="Total Amount || "  , bg='white')

    def defining_middle_controls(self):
        # Middle frame controls
        if len(self.user_taken_books) > 0:

            self.books_taken_options = OptionMenu(self.middle_frame , self.books_that_returned_string, *self.options_book_name)
            self.books_taken_options.configure(bg='white')
            self.books_taken_options.pack(side='right' , padx=10)
            self.returnbtn = Button(self.middle_frame , text="Return Selected Book" , bg='white',relief='groove' , bd=1)
            self.returnbtn.pack(side='right' , padx=10)
            self.returnbtn.bind("<Enter>" , self.return_btn_hover)
            self.returnbtn.bind("<Leave>" , self.return_btn_leave)
            self.books_taken_options.bind("<Enter>" , self.options_hover)
        if len(self.books_to_take) > 0:

            self.books_to_take_options  = OptionMenu(self.middle_frame , self.books_to_rent_string, *self.options_book_return)
            
            self.rentbtn = Button(self.middle_frame , text="Rent Selected Book" , bg='white' ,relief='groove' , bd=1, command=self.rent_the_book_rent_button_clicked)
            self.rentbtn.pack(side='left' , padx=10)
            self.rentbtn.bind("<Enter>" , self.rent_btn_hover)
            self.rentbtn.bind("<Leave>" , self.rent_btn_leave)
            
        # self.returnbtn = Button(self.middle_frame , text="Return Selected Book" , bg='white',relief='groove' , bd=1)
        

        # Setting Hover Functions for diff controls ## used to make the hover effect and other animations
        
        
        



    def defining_bottom_controls(self):
        # Treeview defined for the book details
        self.table = ttk.Treeview(self.lowerframe,  columns=("1" , "2" , "3" ,"4" , "5") , show='headings' , height=5)
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


          
    def rent_the_book_rent_button_clicked(self):
            try:
                self.books_taken_options['menu'].delete(self.books_that_returned_string.get())
                # self.books_to_take_options['menu'].delete(self.books_that_returned_string.get())
                self.books_that_returned_string.set("Choose the book")
                self.book_count +=1
                self.books_taken.config(text="Books Taken || " + str(self.book_count))
                
                # Will be definign the amount phase here
                # Will be defining the fine amount here also
                



            except:
                pass


        # try:
        #     self.books['menu'].delete(self.var_choose.get())
        #     self.var_choose.set("Available Books")
        #     self.bookcount +=1
        #     self.books_label.config(text="Books Taken || " + str(self.bookcount))
        #     self.total_check_amount = 0
        #     self.fine_amount = 0
        #     for item in self.table.get_children():
        #         self.table.delete(item)
        #     for lines in returned_data:
        #         self.returned_data = lines
                
        #         current_date = datetime.today().date()
        #         date2 = self.returned_data[3]
        #         date2 = parser.parse(date2).date()
        #         self.date_diff = self.check_amount(current_date , date2)
        #         self.total_check_amount  += self.date_diff
        #         self.amount_label.config(text="Amount Incured || " + str(self.total_check_amount))
        #         self.table.insert('' , 'end' , text="1" , values=(self.returned_data[0] , self.returned_data[1] , self.returned_data[2], self.returned_data[3],self.date_diff))
        # except :
        #     print("Error hai")

    
    def placing_controls(self):
       
        
       
        
        
        # Placing the bottom controls
        self.lowerframe.pack(fill=BOTH , expand=True , side=TOP)
        self.table.pack(fill=BOTH , side=TOP ,expand=True)
        # Calling the main app to run
        self.user_dashboard.mainloop()
        self.set_username()



""" Ui for the librarian Dashboard  """
class librariandashboard():

    def __init__(self, username , usernames ) -> None:
        self.librarian_dashboard = Tk()
        self.librarian_dashboard.title("Library Manager - Librarian")
        self.librarian_dashboard.geometry("1100x600")
        self.librarian_dashboard.configure(bg='white')
        self.librarian_dashboard.iconbitmap(r"Views\app_icon.ico")
        
        self.myusername  = username
        # usernames the books and other bookkrelated data will be saved here usign the list 
        self.received_raw_user_details  = usernames
        self.user_details  = [] 
        
        self.setting_user_details()
    
    
    # place to define the functions to be called for setting the usernames and  other user details
    def setting_user_details(self):
        for names in self.received_raw_user_details:
            self.user_details.append(names[0])
        
        self.usernames = StringVar()
        self.usernames.set("Choose user :")
        self.getusername_for_contactdetails   = StringVar()
        self.getusername_for_contactdetails.set("Select Username")


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
        self.sendmessage.delete(0 , "end")
        self.sendmessage.insert(0  ,"Enter Notification message for user :")
        self.sendmessage.configure(fg='grey')
        self.librarian_dashboard.focus()

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
        self.users_text = Label(self.numberofusers , text="Total Users | 22")
        self.numberofbooks = Frame(self.middle_frame , height=100  , padx=40 , pady=20)
        # self.books_count  =Label(self.numberofbooks , height=20 , bg='blue' , padx=20 , pady=20)
        self.books_count  =Label(self.numberofbooks , text="Total Books | 300")
        self.borrowedbooks  =Frame(self.middle_frame , height=100 , padx=40 , pady=20)
        self.borrowedbooks_count  = Label(self.borrowedbooks , text="Borrowed Books | 100")
        self.overduebooks = Frame(self.middle_frame , height=100,  padx=40 , pady=20)
        self.overduebooks_count = Label(self.overduebooks , text="Overdue Books | 50")
        self.total_amount = Frame(self.middle_frame , height=100 , width=100  , padx=40 , pady=20)
        self.amount_incured = Label(self.total_amount , text="Amount Incured | 3000")
        
        # Controls to add the book to any user
        """ Temporary function after will be controlled using a function and strign var will only be defined here"""
        self.book_data = StringVar()
        self.book_data.set("Choose book to add :")

        self.available_books  = ['book1' , 'book2' , 'book3']
        self.available_books_list  = OptionMenu(self.lowerframe , self.book_data , *self.available_books)
        self.setbook = Button(self.lowerframe ,text="Add Book to User" )
        
        self.usernames_option = OptionMenu(self.lowerframe , self.usernames , *self.user_details )

        # second user select for the returning book : 
        self.return_book_data =StringVar()
        self.return_book_data.set("Choose book to return")
        self.return_books = ["asdf" , "asdfasdf" , "dasfafasdf", "4563456"]
        self.return_books_list = OptionMenu(self.lowerframe , self.return_book_data , *self.return_books)
        self.returnbook_btn = Button(self.lowerframe , text="Return Selected Book")

        # Controls to send message to the user 
        self.sendmessage  =Entry(self.sendmessageframe , fg='gray' , width=50)
        self.sendmessage.insert(0 , "Enter Notification message for user :")
        self.sendmessage.bind("<FocusIn>" , self.messageboxfocus)

        self.message_usernames = StringVar()
        self.message_usernames.set("User for notification : ")

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
        self.usernamegetbtn = Button(self.getdetailsframe , text="Get User Details")
        
  
    
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
        self.return_books_list.pack(side='left' , padx=5)
        self.returnbook_btn.pack(side='left' , padx=5)

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
    

if __name__ == '__main__':
    # name  = librariandashboard()
    name  = Userdashboard("vinay Pant")