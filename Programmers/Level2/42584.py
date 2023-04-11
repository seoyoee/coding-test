def solution(prices):
    n = len(prices)
    answer = []
    
    for i in range(n):
        count = 0
        now = prices[i]
        for j in range(i+1, n):
            count += 1
            if now > prices[j]:
                break
        answer.append(count)
        
    return answer