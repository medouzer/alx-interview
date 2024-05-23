#!/usr/bin/python3
"""UTF-8 Validation"""

def check_utf(num):
    """check if is utf or not"""
    i = 7
    while (num & 1 << i):
        i -=1
    return 7 - i


def validUTF8(data):
    """method validUTF8"""
    n_bytes = 0
    for item in data:
        if n_bytes == 0:
            n_bytes = check_utf(item)
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if ( not (item & 1 << 7) or (item & 1 << 6)):
                return False
        n_bytes -= 1
    
    return n_bytes == 0
