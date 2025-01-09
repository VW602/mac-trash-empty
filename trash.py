"""
vw602- Gabriel Sanchez

"""
import os

def empty_trash():
    try:
        # Use os.system to execute the shell command to remove all files and directories in the Trash folder.
        # The "-rf" options in the rm command mean:
        #   -r: Remove directories and their contents recursively.
        #   -f: Force the removal without confirmation.
        os.system("rm -rf ~/.Trash/*")
        
        # Print a success message if the trash was emptied successfully.
        print("Trash emptied successfully.")
    except Exception as e:
        # Handle any exceptions that might occur, such as permission issues or other errors.
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Call the empty_trash function when the script is executed.
    empty_trash()
