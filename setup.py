from cx_Freeze import setup, Executable

setup(
    name="Library Manager",
    version="1.0",
    description="Library Manager Using Tkinter Module",
    executables=[Executable("controller.py", base="Win32GUI")]
)

"""  This file is sued for building the main exe of the app without console """
