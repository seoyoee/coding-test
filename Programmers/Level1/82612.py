def solution(price, money, count):
    for i in range(count):
        money -= (i+1) * price
    if money < 0:
        return money * -1
    else:
        return 0