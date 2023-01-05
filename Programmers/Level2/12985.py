def solution(n,a,b):

    for i in range(1, n):
        if a % 2:
            a += 1
        if b % 2:
            b += 1
        a /= 2
        b /= 2
        if a == b:
            return i