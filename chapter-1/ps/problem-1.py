import os
from typing import List

def list_directory_contents(directory_path: str) -> List[str]:
    """
    Prints and returns a list of all files and directories
    in the specified path using os.listdir().

    Args:
        directory_path: The path of the directory to list.
    
    Returns:
        A list of strings containing the names of the entries
        in the directory.
    """
    try:
        # os.listdir() returns a list of all entries (files and subdirectories)
        contents = os.listdir(directory_path)
        
        print(f"--- Contents of '{directory_path}' ---")
        if contents:
            for item in contents:
                print(item)
        else:
            print("The directory is empty.")
            
        print("---------------------------------------")
        return contents
        
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# --- Example Usage ---

# 1. List the contents of the current working directory (CWD)
# The '.' represents the current directory.
current_dir = 'D:\Backend'
list_directory_contents(current_dir)

# 2. Example with a specific path (you can change this to a path on your system)
# Replace 'C:/Users/YourName/Documents' with an actual path to test it.
# specific_path = 'C:/Users/YourName/Documents' 
# list_directory_contents(specific_path)