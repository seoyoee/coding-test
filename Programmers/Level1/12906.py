from collections import deque

def solution(arr):
    answer = []
    queue = deque()
    
    for n in arr:
        if (not queue) or (n != num):
            queue.append(n)
            num = n
    
    answer = list(queue)
    return answer