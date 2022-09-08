def solution(n):
    x = n ** (1/2)
    if x % 1:
        return -1
    else:
        return (x+1) ** 2