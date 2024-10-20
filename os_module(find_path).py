import os

# Get the directory you want to list (you can change this to any path)
directory = input("Enter the directory path: ")

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory)

    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{directory}' does not exist.")

except PermissionError:
    print(f"Error: You do not have permission to access '{directory}'.")

except Exception as e:
    print(f"An error occurred: {e}")
