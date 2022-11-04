T = int(input())
for test_case in range(1, T + 1):
    s = input()
    for i in range(1, 11):
        pattern = True
        for j in range(30//i - 1):
            if s[i*j : i*(j+1)] != s[i*(j+1):i*(j+2)]:
                pattern = False
                break
        if pattern:
            print("#" + str(test_case) + " " + str(i))
            break