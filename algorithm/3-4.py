# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())

count = 0

while n != 1:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)

# N이 K의 배수가 되도록 한 번에 만드는 방법
while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없ㅇ르 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    count += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
count += (n - 1)

print(count)