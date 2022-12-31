def solution(k, score):
    answer = []
    honor = []
    
    for i in score:
        if len(honor) < k:
            honor.append(i)
        elif i > min(honor):
            honor[0] = i
        honor.sort()
        answer.append(honor[0])
        
    return answer