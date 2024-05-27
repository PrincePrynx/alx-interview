#!/usr/bin/python3
"""Module returns a list of lists of integers
representing the Pascal’s triangle of n"""

# Define a function named `pascal_triangle` that takes an integer `n` as its parameter.
def pascal_triangle(n):
    """lists a list of integers """
    
    # If `n` is less than or equal to 0, return an empty list since a Pascal's triangle cannot be generated.
    if n <= 0:
        return []

    # Initialize an empty list `triangle` that will store the rows of Pascal's triangle.
    triangle = []
    
    # Loop from 0 to n-1 to generate each row of the triangle.
    for i in range(n):
        # Start each row with a list containing a single element 1 (the first element is always 1).
        row = [1]
        
        # If `i` is greater than 0, compute the intermediate elements of the row.
        if i > 0:
            # Loop through each position in the row from 1 to `i-1`.
            for j in range(1, i):
                # Each element (except the first and last) is the sum of the two elements above it.
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # Append 1 to the end of the row (the last element is always 1).
            row.append(1)
        
        # Add the completed row to the `triangle` list.
        triangle.append(row)

    # Return the completed list of lists representing Pascal's triangle.
    return triangle

