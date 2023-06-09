import sys
# sys.path.append('LM_Custom_UI\Views')
sys.path.append('Views')

# import login_page
# import register_page  ## Both pages are imported using sys and modifiying the Path 

''' The above code will be used in case we have to modify the paht for importing the file 
For now going forward with the package route and makignt he __init__.py file inside the folders'''

from Views.login_page import Login_page
from Views.register_page import Register_page
from Views.dashboard import User_Dashboard , Dashboard
import Models.database as database
from Views import colors as colors
from Views import styles as styles
from tkinter import messagebox
from pubsub import pub


def login_page_called():
    global login
    login = Login_page(300 , 400)
    login.defining_controls()
    login.placing_controls()


def calling_librarian_dashboard(username , user_details , book_to_take):
    print('Librarian Dashboard Called')

def calling_user_dashboard(username , taken_books , available_books , notification_string = ""):
    global user_dashboard
    user_dashboard = User_Dashboard(1000 , 500 , username=username , taken_books=taken_books , available_books=available_books , notification_string=notification_string)
    user_dashboard.defining_controls()
    user_dashboard.placing_controls()



def check_login_credentials(user_details):
    username = user_details.split(",")[0]
    password=  user_details.split(",")[1]
    returned_data  = database.checking_login_details(username , password)
    if returned_data == False:
        messagebox.showerror("Library Manager" , "Wrong Username or Password")
    elif returned_data == 'librarian':
        login.closing_app()
        book_to_take  = database.available_book_details()
        available_books  = database.available_book_details()
        user_details  = database.get_usernames()
        calling_librarian_dashboard(username , user_details , book_to_take)
    elif returned_data == 'user':
        taken_books = database.get_book_details(username)
        available_books  = database.available_book_details()    
        available_books  = database.available_book_details()
        # Getting the notification String 
        notification_string = database.check_notification(username)
        login.closing_app()
        calling_user_dashboard(username , taken_books, available_books , notification_string)

def calling_register_page(register_data ):
    global register_page_1
    register_page_1   = Register_page(300 , 450)
    register_page_1.defining_controls()
    register_page_1.placing_controls()
    login.closing_app()


def renting_book(book_details):
    username =  book_details.split(',')[0]
    book_name  = book_details.split(',')[1]
    print(username)
    print(book_name)
    returned_book  = database.rent_book(username  = username  , book_name= book_name)
    user_dashboard.taken_books_user.append(returned_book[0][0])
    user_dashboard.taken_books_table.append(returned_book[0])
    user_dashboard.filling_treeview()



## Message Receiving from View Modules :  
pub.subscribe(check_login_credentials , 'login_details')
pub.subscribe(calling_register_page ,  'register_page_called')
pub.subscribe(renting_book , 'add_book')


if __name__ == '__main__':
    login_page_called()    
    