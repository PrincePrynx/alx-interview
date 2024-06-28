#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Validate if a given data set represents a valid UTF-8 encoding.
    
    :param data: List of integers
    :return: True if data is a valid UTF-8 encoding, else False
    """
    n_bytes = 0

    for num in data:
        byte = num & 0xFF  # Get the last 8 bits

        if n_bytes == 0:
            # Count the number of leading 1's
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7) != 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
        n_bytes -= 1

    return n_bytes == 0

if __name__ == "__main__":
    import sys
    import os
    # Basic usage and testing
    print(validUTF8([197, 130, 1]))  # True
    print(validUTF8([235, 140, 4]))  # False
