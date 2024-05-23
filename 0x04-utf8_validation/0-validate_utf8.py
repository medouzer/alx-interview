#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """method validUTF8"""
    try:
        bytes(data).decode('utf-8')
        return True
    except Exception:
        return False
