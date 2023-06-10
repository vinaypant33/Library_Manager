import sys
from cx_Freeze import setup, Executable

# Replace "my_app.py" with the name of your main script
exe = Executable(
    script="controller.py",
    base=None,
    icon=r'C:\Users\Vinay\Desktop\git_hub\Library_Manager\code_base\custom_ui\Assets\app_icon.ico'  # Optionally, specify the path to the application icon
)

setup(
    name="Library_Manager",
    version="1.0",
    description="Library Manager - using tkinter and sqlite",
    executables=[exe],
    options={
        "build_exe": {
            "packages": [],
            "include_files": []  # Add any additional files or data here
        }
    }
)


## use python setup.py build for building the app 
