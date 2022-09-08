def solution(n, m):
    a = max([x for x in range(1, min(n,m)+1) if not (n%x or m%x)])
    b = n*m/a
    
    return [a, b]