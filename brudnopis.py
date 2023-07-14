# for testing code snippets


def get_py_files(directory):
    py_files = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".py"):
            py_files.append(file_name)
    return py_files

def format_files_as_string(file_list):
    return " ".join(file_list)

# Specify the directory path to scan
directory_path = "./"  # Replace with your desired directory path

# Get the .py files in the directory
py_files = []
for file_name in os.listdir(os.path.abspath(__file__)):
    if file_name.endswith(".py"):
        py_files.append(file_name)

# Format the files as a string
formatted_string = format_files_as_string(py_files)

# Print the result
print(formatted_string)