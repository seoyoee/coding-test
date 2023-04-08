from collections import deque

def solution(priorities, location):
    answer = 0
    wait = deque(list(enumerate(priorities)))
    
    while wait:
        now = wait.popleft()
        for doc in wait:
            if now[1] < doc[1]:
                wait.append(now)
                break
        else:
            answer += 1
            if now[0] == location:
                return answer