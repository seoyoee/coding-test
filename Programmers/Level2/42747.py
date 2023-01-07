def solution(citations):
    n = len(citations)
    
    for i in reversed(range(n+1)):
        count = 0
        
        for c in citations:
            if c >= i:
                count += 1
        
        if count >= i:
            return i