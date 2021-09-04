import sys
import os
from cx_Freeze import setup, Executable

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
# print(PYTHON_INSTALL_DIR)
# os.environ['TCL_LIBRARY'] = "C:\\Users\\Mike\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tcl86t.dll"
# os.environ['TK_LIBRARY'] = "C:\\Users\\Mike\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tk86t.dll"
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["numpy", "pandas", "matplotlib", "os"],
    "includes": ["tkinter"],
    "include_files": [
        "data.tsv",
        # os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl86t.dll'),
        # os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk86t.dll'),
        os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6'),
        os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6'),
        # "C:\\Users\\Mike\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tcl86t.dll",
        # "C:\\Users\\Mike\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tk86t.dll",
        # "C:\\Users\\Mike\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6",
        # "C:\\Users\\Mike\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"
    ]
}
#build_exe_options = {"packages": [], "includes": ["tkinter"], "include_files": ["C:\\Users\\Mike\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tcl86t.dll","C:\\Users\\Mike\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs\\tk86t.dll"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Water",
        version = "1.1.0",
        author = "Олександр Кушка",
        description = "Machine learning application to calculate water consumption per second",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Cold Water.py",
                                  base=base,
                                  icon="icon.ico")])

