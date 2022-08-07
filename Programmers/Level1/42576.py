def solution(participant, completion):
    answer = ''
    dic = {p:0 for p in participant}
    
    for p in participant:
        dic[p] += 1
    for c in completion:
        dic[c] -= 1
    for d in dic:
        if dic[d] != 0:
            answer = d
    return answer