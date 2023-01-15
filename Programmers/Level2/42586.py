def solution(progresses, speeds):
    days = []
    answer = {}
    
    for p,s in zip(progresses, speeds):
        days.append(-((p - 100) // s))
    
    answer[days[0]] = 1
    
    for i in range(1, len(days)):
        if days[i] < days[i - 1]:
            days[i] = days[i - 1]
        if days[i] in answer:
            answer[days[i]] += 1
        else:
            answer[days[i]] = 1
    
    return list(answer.values())