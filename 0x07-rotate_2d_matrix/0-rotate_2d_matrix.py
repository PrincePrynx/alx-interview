#!/usr/bin/python3
'''2D matrix'''

def rotate_2d_matrix(matrix):
    '''Rotates a 2D matrix 90° clockwise.
    Returns: Nothing'''
    
    # Initialize pointers for the left and right edges of the matrix
    left, right = 0, len(matrix) - 1

    # Loop until the pointers meet in the middle
    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            
            # Save the top-left value
            topLeft = matrix[top][left + i]
            
            # Move bottom-left to top-left
            matrix[top][left + i] = matrix[bottom - i][left]
            
            # Move bottom-right to bottom-left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            
            # Move top-right to bottom-right
            matrix[bottom][right - i] = matrix[top + i][right]
            
            # Move saved top-left to top-right
            matrix[top + i][right] = topLeft
        
        # Move the left and right pointers inward
        right -= 1
        left += 1

