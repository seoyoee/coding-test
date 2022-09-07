def solution(arr):
    answer = []
    
    for n in arr:
        if (not answer) or (n != num):
            answer.append(n)
            num = n
    
    return answer