#!/usr/bin/python3
"""
0x01. Lockboxes
"""

from collections import deque


def do_action(my_queue, boxes, index):
    """function do_action"""
    if index in my_queue or index >= len(boxes):
        return
    my_queue.append(index)
    for key in boxes[index]:
        do_action(my_queue, boxes, key)
        
 
def canUnlockAll(boxes):
    """function canUnlockAll"""
    my_queue = deque()
    do_action(my_queue, boxes, 0)
    for i in range(0, len(boxes)):
        if (i not in my_queue):
            return False
    return True
