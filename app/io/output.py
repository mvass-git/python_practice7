def write_console(data):
    """
    Writes data to the console.

    This function writes data to the console, typically for displaying output to the user.

    Args:
        data (str): The data to be written to the console.

    Returns:
        None
    """
    print(data)


def write_file_python(file_path, data):
    """
    Writes data to a file with Python.

    This function writes data to a file in the Python language format.

    Args:
        file_path (str): The path to the Python file.
        data (str): The data to be written to the file.

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        file.write(data)
