#!/usr/bin/python3
"""
0-pascale_triangle.py
"""

def make_arr(arr, n):
    """this also"""
    
    table = [1]
    if(n == 0):
        return (table)
    for index in range(1, n):
        table.append(arr[index - 1] + arr[index ])
    table.append(1)
    return (table)

def pascal_triangle(n):
    """this function to"""

    if (n <= 0):
        return []
    res = [[1]]
    for index in range(1, n):
        res.append( make_arr(res[index - 1], index) )
    return (res)
