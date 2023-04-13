# Importing Premade Packages
import sqlite3
import datetime


# Making data base or connecting with it 
conn  = sqlite3.connect('library_management.db')
c  = conn.cursor()

# Function always to be called to save the details to the database
def saving_details():
    conn.commit()

# Function to check the user in the database
def checking_login_details(username , password):
    c.execute('SELECT * FROM users WHERE username="%s" AND password="%s"' % (username, password))
    list = c.fetchall()
    # print(list)
    # print(list[0][2])
    if len(list) > 0:
        if list[0][2] == 'librarian':
            return 'librarian'
        elif list[0][2] == 'user':
            return 'user'
    elif len(list) == 0:
        return False

# Function to get the  user details in the form of books details
def get_book_details(username):
    c.execute('SELECT * FROM books WHERE rented_user = "%s";' %(username))
    count_list = c.fetchall()
    return count_list

def available_book_details():
    c.execute('SELECT * FROM books WHERE rented_user IS NULL;')
    list  = c.fetchall()
    return list
    
# Function to register new user
def registering_new_user(username , password , secret_answer):
    c.execute('INSERT INTO users (username,password,user_type,secret_answer) VALUES ( "%s", "%s", "user", "%s");' %(username ,password , secret_answer))
    saving_details()

# Function to reterive password details
def reteriving_password_details(username , secretanswer ):
    c.execute('SELECT * FROM users WHERE username="%s" AND secret_answer="%s"' % (username, secretanswer))
    list = c.fetchall()
    if len(list) > 0:
        return(list[0][1])
    else:
        return False
    
# FUnction to get the usernames for the librarian Dashboard
def get_usernames():
    c.execute('SELECT * FROM users WHERE user_type  =  "user";')
    list = c.fetchall()
    return list
    
# Function to add book to the database
def adding_book(book_name  , book_publication , author_name , book_company):
    c.execute('INSERT INTO books ( book_name , book_publication , book_author , book_company) VALUES ("%s" , "%s" , "%s" , "%s");' %(book_name , book_publication ,author_name ,book_company))
    saving_details()
    

# Function to rent book for the user from the book name
def rent_book(username, book_name):
    current_date  = datetime.date.today()
    c.execute('UPDATE books SET rented_date = "%s" WHERE book_name = "%s";' %(current_date , book_name))
    saving_details()
    c.execute('UPDATE books SET rented_user = "%s" WHERE book_name = "%s";' %(username , book_name))
    saving_details()
    c.execute('SELECT * from books WHERE book_name = "%s";' %(book_name))
    list = c.fetchall()
    return list

def return_book(book_name):
    c.execute('UPDATE books SET rented_date = NULL WHERE book_name = "%s";' %(book_name))
    saving_details()
    c.execute('UPDATE books SET rented_user = NULL WHERE book_name = "%s";' %(book_name))
    saving_details()
    
# Function to check the notification string from the database
def check_notification(username):
    c.execute('SELECT * FROM users WHERE username = "%s";' %(username))
    list = c.fetchall()
    return(list[0][4])
    
def clearing_notification(username):
    c.execute('UPDATE users SET notification = NULL WHERE username = "%s";' %(username))
    saving_details()

def setting_notification(username ,  text_message):
    c.execute('UPDATE users SET notification = "%s" WHERE username ="%s";' %(text_message, username))
    saving_details()
    

