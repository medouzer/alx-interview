#!/usr/bin/python3

from collections import deque


def do_action(my_queue, boxes, index):
    if index in my_queue or index >= len(boxes):
        return
    my_queue.append(index)
    for key in boxes[index]:
        do_action(my_queue, boxes, key)
        
 
def canUnlockAll(boxes):
    my_queue = deque()
    do_action(my_queue, boxes, 0)
    for i in range(0, len(boxes)):
        if (i not in my_queue):
            return False
    return True
