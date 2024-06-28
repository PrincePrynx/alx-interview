#!/usr/bin/python3
"""
Main script to test UTF-8 validation
"""

from utf8_validator import validUTF8

def main():
    test_cases = [
        ([197, 130, 1], True),
        ([235, 140, 4], False),
        ([240, 162, 138, 147], True),
        ([145], False),
        ([0], True),
        ([248, 130, 130, 130], False)
    ]

    for i, (data, expected) in enumerate(test_cases):
        result = validUTF8(data)
        print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")

if __name__ == "__main__":
    main()
