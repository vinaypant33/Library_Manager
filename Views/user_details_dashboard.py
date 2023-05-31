import tkinter
from tkinter import *
from tkinter import ttk


# Class 
class User_details():
    
    def __init__(self , *book_name) -> None:
        self.user_details  = Tk()
        self.user_details.geometry("600x400")
        self.user_details.configure(bg='white')
        self.user_details.iconbitmap(r"Views\app_icon.ico")
        # self.user_details.resizable(0,0)
        self.user_details.title("Library Manager  -  User Details")
        self.temp_books_to_take  = []
        self.temp_books_to_take = book_name
        # print(book_name)
        self.taken_book_details = []
        self.count = len(self.temp_books_to_take)
        print(self.count)
        for book_name in book_name:
            self.taken_book_details.append(book_name)
        
        
        
    #  def filling_treeview(self):
    #     # self.table.insert('' ,'end' , text="1" , values=(name  , publication , author  , date  , rupees))
    #     for book_name in self.temp_books_taken_by_user:
    #         self.date_difference = self.calculating_amount(book_name[4])
    #         self.date_difference = int(self.date_difference)
    #         if self.date_difference == 0:
    #             self.temporary_amount = 12
    #             self.amount_count+=12
    #         elif  7 > self.date_difference > 0 :
    #             self.temporary_amount  = 12 * self.date_difference
    #             self.amount_count+= self.temporary_amount
    #         else:
    #             # self.date_difference  > 12
    #             self.temporary_amount = 12 * self.date_difference + 100
    #             self.amount_count+= self.temporary_amount
            
    #         self.table.insert('' ,'end' , text="1" , values=(book_name[0]  , book_name[1] , book_name[2]  , book_name[4]  , self.temporary_amount))
    #         self.updating_controls()
        
    def defining_controls(self):
        
        self.table = ttk.Treeview(self.user_details,  columns=("1" , "2" , "3" ,"4") , show='headings' , height=5)
        self.table.column("# 1" , anchor=CENTER)
        self.table.heading("# 1", text="Book Name")
        self.table.column("# 2", anchor=CENTER)
        self.table.heading("# 2", text="Book Publication")
        self.table.column("# 3", anchor=CENTER)
        self.table.heading("# 3", text="Book Author")
        self.table.column("# 4", anchor=CENTER)
        self.table.heading("# 4", text="Rented Date")
        
        self.table.pack(fill=BOTH , expand=True)
        for book_name in self.temp_books_to_take:
              self.table.insert('' ,'end' , text="1" , values=(book_name[0][0], book_name[0][1] , book_name[0][2]  , book_name[0][4]))
        
        
        # Calling the main App
        self.user_details.mainloop()
        
# if __name__ == '__main__':
#     temp =User_details()
#     temp.defining_controls()
     