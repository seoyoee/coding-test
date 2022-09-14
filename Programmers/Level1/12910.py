def solution(arr, divisor):
    return sorted([x for x in arr if not x % divisor]) or [-1]