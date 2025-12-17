import pyttsx3
engine = pyttsx3.init()

engine.say("""What it does: The os.listdir(path) function returns a list of strings, where each string is the name of a file or a subdirectory found in the directory specified by path.

What it returns: It provides only the names of the entries, not the full path. To get the full path for each item, you would typically use os.path.join(directory_path, item).

Default Behavior: If you call it without an argument, like os.listdir(), it lists the contents of the Current Working Directory (CWD).

Would you like to try a different approach, such as using os.walk() to recursively list files in subdirectories, or using the modern pathlib module?""")
engine.runAndWait()