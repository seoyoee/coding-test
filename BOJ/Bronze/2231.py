def digitSum(n):
    for i in range(1, n):
        sum = 0
        sum += i
        j = i
        while j:
            sum += j % 10
            j //= 10
        if sum == n:
            return i
    return 0

if __name__ == '__main__':
    n = int(input())
    print(digitSum(n))