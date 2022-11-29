def solution(n):
    num = []
    answer = 0
    
    while n:
        num.append(n % 3)
        n //= 3
    
    num.reverse()
    
    for i in range(len(num)):
        answer += num[i] * 3 ** (i)
    
    return answer