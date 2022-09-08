def binary(arr, bi, n):
    for i in range(n):
        num = arr[i]
        for j in range(n):
            bi.insert(i*n, num%2)
            num //= 2

def solution(n, arr1, arr2):
    bi1 = []
    bi2 = []
    answer = [""] * n

    binary(arr1, bi1, n)
    binary(arr2, bi2, n)

    for i in range(n):
        for j in range(n):
            if bi1[i*n+j] or bi2[i*n+j]:
                answer[i] += "#"
            else:
                answer[i] += " "
    
    return answer