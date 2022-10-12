def solution(n):
    
    n1 = bin(n)
    count = n1.count("1")
    
    while True:
        n += 1
        n2 = bin(n)
        if n2.count("1") == count:
            return n