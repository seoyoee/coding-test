def solution(N, stages):
    player = [0] * (N + 1)
    fail = []
    
    for stage in stages:
        for i in range(0, stage):
            player[i] += 1
    
    for j in range(N):
        if player[j]:
            fail.append(stages.count(j+1) / player[j])
        else:
            fail.append(0)
    
    s = sorted(range(N), key=lambda k: fail[k], reverse=True)
    return [x+1 for x in s]