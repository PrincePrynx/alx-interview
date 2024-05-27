#!/usr/bin/python3
"""
0-main
"""

# Importing the `pascal_triangle` function from the module `0-pascal_triangle`.
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Function to print the Pascal's triangle.
    """
    # Iterate over each row in the triangle.
    for row in triangle:
        # Format each row as a string with elements separated by commas and enclosed in square brackets.
        print("[{}]".format(",".join([str(x) for x in row])))

# If this script is executed as the main program (not imported as a module).
if __name__ == "__main__":
    # Call the `pascal_triangle` function with 5 as an argument to generate the first 5 rows of Pascal's triangle.
    # Pass the generated triangle to the `print_triangle` function to print it.
    print_triangle(pascal_triangle(5))

