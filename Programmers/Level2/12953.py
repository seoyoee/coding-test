def solution(arr):
    LCM = arr[0]
    
    for i in range(len(arr)):
        GCD = gcd(LCM, arr[i])
        LCM *= arr[i] // GCD
    
    return LCM

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)