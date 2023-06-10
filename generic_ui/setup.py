from cx_Freeze import setup, Executable

setup(
    name="Library Manager",
    version="1.0",
    description="Library Manager Using Tkinter Module",
    executables=[Executable("controller.py", base="Win32GUI")]
)

"""  This file is sued for building the main exe of the app without console """


# This code can also be used for the future builds : 

# import sys
# from cx_Freeze import setup, Executable

# # Replace "my_app.py" with the name of your main script
# exe = Executable(
#     script="controller.py",
#     base=None,
#     icon=None  # Optionally, specify the path to the application icon
# )

# setup(
#     name="MyApp",
#     version="1.0",
#     description="My Tkinter Application",
#     executables=[exe],
#     options={
#         "build_exe": {
#             "packages": [],
#             "include_files": []  # Add any additional files or data here
#         }
#     }
# )



# To run the application :  

# Navigate to the  directory and run this command : python setup.py build