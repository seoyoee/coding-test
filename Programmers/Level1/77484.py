def solution(lottos, win_nums):
    zeros = lottos.count(0)
    rights = len(list(set(lottos) & set(win_nums)))
    if rights < 2:
        min = 6
    else:
        min = 7 - rights
    if rights + zeros < 2:
        max = 6
    else:
        max = 7 - (rights + zeros)
    
    answer = [max, min]
    return answer