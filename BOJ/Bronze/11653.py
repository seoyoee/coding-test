n = int(input())
i = 2

while i < n:
    if n % i:
        i += 1
    else:
        print(i)
        n //= i
        i = 2

if n != 1:
    print(n)