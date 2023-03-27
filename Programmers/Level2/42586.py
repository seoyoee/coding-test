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

def solution(progresses, speeds):
    days = []
    answer = []
    
    for i in range(len(progresses)):
        days.append(-((progresses[i] - 100) // speeds[i]))
    print(days)
    
    k = 0
    for i in range(len(days)):
        if i == 0 or days[i] > k:
            answer.append(1)
            k = days[i]
        else:
            answer[-1] += 1
    
    return answer