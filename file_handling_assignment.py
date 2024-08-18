# file_handling_assignment.py

def create_file():
    try:
        # Create and open the file in write mode
        with open("my_file.txt", 'w') as file:
            # Write lines to the file
            file.write("This is the first line of text.\n")
            file.write("Here is the second line with a number: 12345.\n")
            file.write("Third line, with some more text.\n")
        print("File created and written successfully.")
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error occurred while creating/writing the file: {e}")
    finally:
        print("Create file operation complete.")

def read_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", 'r') as file:
            # Read and display the contents of the file
            content = file.read()
            print("\nFile Contents:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading the file: {e}")
    finally:
        print("Read file operation complete.")

def append_to_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", 'a') as file:
            # Append lines to the file
            file.write("Appending a new line of text.\n")
            file.write("Adding another line with some more text.\n")
            file.write("Finally, a third appended line.\n")
        print("File appended successfully.")
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("Append file operation complete.")

# Execute the functions
create_file()
read_file()
append_to_file()
read_file()  # Read the file again to show the appended content
