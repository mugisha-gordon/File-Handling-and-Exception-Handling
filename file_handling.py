def modify_content(content):
    """
    Function to modify the file content.
    Here, I’ll make a simple modification: convert everything to uppercase.
    You can change this to anything (e.g., add line numbers, replace words, etc.).
    """
    return content.upper()


try:
    # Step 1: Ask user for a filename
    filename = input("Enter the name of the file you want to read: ")

    # Step 2: Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Step 3: Modify the content
    modified_content = modify_content(content)

    # Step 4: Write modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"✅ File successfully modified and saved as '{new_filename}'")

except FileNotFoundError:
    # Step 5: Handle case where file doesn’t exist
    print("❌ Error: The file you entered does not exist.")
except PermissionError:
    # Step 6: Handle case where file cannot be read (permissions issue)
    print("❌ Error: You do not have permission to read this file.")
except Exception as e:
    # Step 7: Handle any other unexpected errors
    print(f"❌ An unexpected error occurred: {e}")
