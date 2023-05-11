def solution(elements):
    n = len(elements)
    result = set()
    
    for i in range(n):
        sum = 0
        for j in range(n):
            if i + j < n:
                sum += elements[i + j]
            else:
                sum += elements[i + j - n]
            result.add(sum)
    
    return len(result)