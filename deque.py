'''
Deques (abbreviation of double-ended queues) are generalizations of stacks and queues. In general computer science, they are also referred to as
head-tail linked lists. Generally optimized for O(1) append and pop operations to beginning and end of list, compared to an average of O(n) for
regular lists.

'''

from collections import deque

queue = deque([1, 2, 3, 4, 5])
print(queue)
print(queue[2])

queue.appendleft(0)
print(queue)
queue.popleft()
print(queue)
queue.rotate() # Rotates array to right, default = 1, left with negative numbers
print(queue)
queue.rotate(-2)
print(queue)
