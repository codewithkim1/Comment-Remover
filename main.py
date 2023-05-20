import re
from tkinter import Tk, filedialog

def remove_comments(code):
    # Regular expression pattern to match comments in Python, C/C++, PHP, and SQL code
    pattern = r"(#.*)|(\"{3}[\s\S]*?\"{3})|(\"[\s\S]*?\")|(\/\/.*)|(\/\*[\s\S]*?\*\/)"

    # Remove comments using regular expression substitution
    code_without_comments = re.sub(pattern, "", code)

    return code_without_comments


def process_file():
    # Create Tkinter root window
    root = Tk()
    root.withdraw()

    # Select the input file
    input_file_path = filedialog.askopenfilename(title="Select Input File")
    if not input_file_path:
        print("No input file selected.")
        return

    # Select the output file
    output_file_path = filedialog.asksaveasfilename(title="Save Output File")
    if not output_file_path:
        print("No output file selected.")
        return

    # Read the input file
    with open(input_file_path, 'r') as input_file:
        code = input_file.read()

    # Remove comments from the code
    code_without_comments = remove_comments(code)

    # Write the modified code to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(code_without_comments)

    print("Comments removed. Output file created: " + output_file_path)


# Example usage
process_file()
