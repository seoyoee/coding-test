def solution(X, Y):
    x = {}
    y = {}
    pair = {}
    answer = ""
    
    for i in list(X):
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    
    for i in list(Y):
        if i in y:
            y[i] += 1
        else:
            y[i] = 1
    
    for i in x:
        if i in y:
            pair[i] = min(x[i], y[i])
            
    num = sorted(pair, reverse=True)
    
    if len(pair):
        if len(pair) == 1 and "0" in num:
            return "0"
        for i in num:
            answer += i * pair[i]
        return answer
    return "-1"