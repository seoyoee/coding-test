def solution(s):
    answer = [0, 0]
    
    while s != "1":
        n = s.count("1")
        answer[1] += s.count("0")
        s = ""
    
        while n > 0:
            s = str(n%2) + s
            n //= 2
        
        answer[0] += 1
        
    return answer