T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    answer = sum([x for x in nums if x % 2])
    print("#" + str(t) + " " + str(answer))