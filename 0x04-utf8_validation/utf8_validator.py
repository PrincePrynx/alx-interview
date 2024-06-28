#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    byte_count = 0  # Number of bytes in the current UTF-8 character

    for i in data:
        if byte_count == 0:  # If we are not in the middle of processing a UTF-8 character
            if i >> 5 == 0b110:  # 2-byte character (starts with 110xxxxx)
                byte_count = 1
            elif i >> 4 == 0b1110:  # 3-byte character (starts with 1110xxxx)
                byte_count = 2
            elif i >> 3 == 0b11110:  # 4-byte character (starts with 11110xxx)
                byte_count = 3
            elif i >> 7 == 0b1:  # Invalid single byte (starts with 1xxxxxxx)
                return False
        else:  # We are in the middle of processing a UTF-8 character
            if i >> 6 != 0b10:  # Continuation bytes must start with 10xxxxxx
                return False
            byte_count -= 1  # One less byte to process for the current character

    return byte_count == 0  # All characters should be completely processed
