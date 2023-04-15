from tkinter import *
from pubsub import sub 



## Importing premade models from previous folders

from Views import loginandregister




class Login_page(loginandregister.LoginScreen):
    
    def __init__(self) -> None:
        super().__init__()