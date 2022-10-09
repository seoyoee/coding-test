def solution(n):
    count = 0
    
    for i in range(1, n+1):
        sum = 0
        num = i
        while sum <= n:
            sum += num
            num += 1
            if sum == n:
                count += 1
    
    return count