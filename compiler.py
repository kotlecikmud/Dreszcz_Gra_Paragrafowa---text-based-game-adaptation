import os
import timeit
import subprocess
from constants import VER_FILE
from datetime import datetime as dt

ICON_FILE = r"_designs/face/icon.ico"


def compile_code():
    # Check for the presence of the icon file
    if not os.path.isfile(ICON_FILE):
        print("\n<!> No icon file found")
        return False  # Return False to indicate failure
    else:
        print(f"\nIcon file found: {ICON_FILE}")

    # Read version number from the version file
    try:
        with open(VER_FILE, 'r') as ver_f:
            __version__ = ver_f.readline().strip()  # Strip the newline character
    except FileNotFoundError:
        print("\n<!> Version file not found")
        return False  # Return False to indicate failure

    # Generate a unique build number using the current date and time
    build_number = dt.now().strftime("%d%m%y%H%M%S")

    print(f"\nCompiling to file: Dreszcz_{__version__}_{build_number}")

    # Get a list of all .py files in the current directory
    py_files = [file for file in os.listdir() if file.endswith('.py') and file != 'compiler.py']

    # Join the .py file names into a single string separated by spaces
    py_files_str = ' '.join(py_files)

    # Create and run the pyinstaller command using the list of .py files and other options
    command = f'pyinstaller --onefile --icon {ICON_FILE} -n Dreszcz_{__version__}_{build_number} {py_files_str}'

    # Execute the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during pyinstaller execution: {e}")
        return False  # Return False to indicate failure

    return True  # Return True to indicate success


# Time the compile_code function
execution_time = timeit.timeit(compile_code, number=1)
print(f"\nExecution time: {execution_time:.2f} seconds")
