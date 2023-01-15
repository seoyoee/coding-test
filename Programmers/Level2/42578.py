def solution(clothes):
    types = {}
    answer = 1
    
    for c in clothes:
        if c[1] in types:
            types[c[1]] += 1
        else:
            types[c[1]] = 1
    
    for t in types.values():
        answer *= t + 1
    
    return answer - 1
        