def solution(k, tangerine):
    answer = 0
    amount = []
    count = 1

    tangerine.sort()

    for i in range(len(tangerine)):
        if i == len(tangerine) - 1:
            amount.append(count)
        elif tangerine[i] == tangerine[i + 1]:
            count += 1
        else:
            amount.append(count)
            count = 1

    amount.sort()

    while k > 0:
        k -= amount.pop()
        answer += 1

    return answer