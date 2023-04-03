def solution(number, limit, power):
    method = []
    
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** (1/2)) + 1):
            if i % j == 0:
                if i != j ** 2:
                    count += 1
                count += 1
        method.append(count)
    
    for i in range(len(method)):
        if method[i] > limit:
            method[i] = power
    
    return sum(method)