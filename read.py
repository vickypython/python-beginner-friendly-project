def read_and_modify_file():
    try:
        # Ask user for the filename
        input_filename = input("Enter the filename to read: ")
        
        # Open and read the file
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.readlines()  # Read all lines into a list
        
        # Modify the content (Example: Convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Create a new filename
        output_filename = "modified_" + input_filename

        # Write the modified content to a new file
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.writelines(modified_content)
        
        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please enter a valid filename.")
    except PermissionError:
        print("Error: Permission denied. You might not have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
