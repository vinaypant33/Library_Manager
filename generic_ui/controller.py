# Importing premade modules
from pubsub import pub
from tkinter import messagebox
# Importing defined Modules
from Views import loginandregister
from Models import database
from Views import dashboard , message_center
from Views import user_details_dashboard
## calling the controls for the views functions``
def calling_login():
    try :
        register.kill_register()        
        forgotscreen.killing_app()
    except:
        print("Error Occured")
    global loginform
    loginform  = loginandregister.LoginScreen()
    loginform.defining_controls()
    loginform.placing_controls()

def calling_register():
    loginform.killing_app()
    global register
    register = loginandregister.RegisterScreen()
    register.define_controls()
    register.place_controls()
    
def calling_forgotscreen():
    loginform.killing_app()
    global forgotscreen
    forgotscreen = loginandregister.ForgotPassword()
    forgotscreen.defining_controls()
    forgotscreen.placing_controls()
    
def calling_librarian_dashboard(username , user_details , available_books):
    global librarian_dashboard 
    librarian_dashboard  = dashboard.librariandashboard(username , user_details , available_books)
    librarian_dashboard.defining_upper_controls()
    librarian_dashboard.defining_middle_controls()
    librarian_dashboard.defining_lower_controls()
    librarian_dashboard.placing_controls()

def calling_user_dashboard(username , taken_books , available_books , notification_string):
    global user_dashboard
    # Send the user_name password and the required book details in this format
    user_dashboard  = dashboard.Userdashboard(username , taken_books ,available_books , notification_string)
    user_dashboard.defining_upper_controls()
    user_dashboard.defining_middle_controls_rentbook()
    user_dashboard.defining_middle_controls_returnbook()
    user_dashboard.defining_lower_controls()
    user_dashboard.placing_controls()
    user_dashboard.starting_app()

# Defining Functions that will be called when pubsubscribe catchs a Message 
def check_login_credentials(login_data): 
    username = login_data.split(",")[0]
    password=  login_data.split(",")[1]
    returned_data  = database.checking_login_details(username , password)
    if returned_data == False:
        messagebox.showerror("Library Manager" , "Wrong Username or Password")
    elif returned_data == 'librarian':
        loginform.killing_app()
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
        loginform.killing_app()
        calling_user_dashboard(username , taken_books, available_books , notification_string)

def registering_new_user(register_data):
    username  = register_data.split(",")[0]
    password  = register_data.split(",")[1]
    secret_question = register_data.split(",")[2]
    database.registering_new_user(username, password , secret_question)
    messagebox.showinfo("Library_Manager" , "New User Registered")
    
def reteriving_user_password(password_details):
    username  = password_details.split(",")[0]
    secret_answer = password_details.split(",")[1]
    password = database.reteriving_password_details(username , secret_answer)
    forgotscreen.setting_password(password)

def calling_login_indifectly():
    calling_login()
    
def saving_book_details(book_data):
    # print(book_data.split(",")[0])
    database.adding_book(book_data.split(",")[0] , book_data.split(",")[1] , book_data.split(",")[2] , book_data.split(",")[3])
    # database.adding_book()

# Calling the database and saving the book
def renting_book(book_details):
    username  = book_details.split(",")[0]
    book_name  = book_details.split(",")[1]
    returned_rented_book = database.rent_book(username , book_name)
    user_dashboard.adding_current_rendted_book(returned_rented_book)

# Calling notification button and setting up the screen
def returning_book(returned_book):
    database.return_book(returned_book)

def renting_book_to_the_user(book_and_username):
    bookname  = book_and_username.split(",")[0]
    username  = book_and_username.split(",")[1]
    database.rent_book(username , bookname)

def sending_notification(username_message):
    username = username_message.split(",")[0]
    text_data  = username_message.split(",")[1]
    database.setting_notification(username , text_data)

# Obselete function to be checked later
def calling_notification(username):
    # x = window_axes.split(",")[0]
    # y = window_axes.split(",")[1]
    # x = int(x)
    # y = int(y)
    # print(x)
    # print(y)
    # message_string  = message_center.Message_box(x , y)
    # message_string.running_app()
    database.clearing_notification(username)


def getting_details(username):
    taken_books = database.get_book_details(username)
    global user_details_for_message
    user_details_for_message  = user_details_dashboard.User_details(taken_books)
    user_details_for_message.defining_controls()

# Use for the pubsub for the diff functions
pub.subscribe(check_login_credentials , "login_data")
pub.subscribe(calling_register ,"register_clicked")
pub.subscribe(calling_forgotscreen , "forgot_clicked")
pub.subscribe(registering_new_user , "register_data")
pub.subscribe(calling_login , "show_login")
pub.subscribe(reteriving_user_password , "reterive_password")
pub.subscribe(calling_login_indifectly, "login_clicked")
pub.subscribe(saving_book_details , "book_details_Save")
pub.subscribe(renting_book , "rent_book")   
pub.subscribe(returning_book , "returned_book")
pub.subscribe(renting_book_to_the_user , "add_book_to_the_user")
pub.subscribe(sending_notification , "notification_alert")
# pub.subscribe(calling_notification, "call_notification")
pub.subscribe(calling_notification , "button_clicked")

# """" Temp function to check the messagebox and make the form appear"""
# def call_message():
#     name  = message_center.Message_box(100,100)
#     name.running_app()
pub.subscribe(getting_details , "Done")

if __name__ == '__main__':
    calling_login()
    """Here we will be calculating the total amount incured and will be saving it in the database"""