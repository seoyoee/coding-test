def solution(today, terms, privacies):
    answer =[]
    dict = {}
    
    y, m, d = map(int, today.split('.'))
    now = y * 12 * 28 + m * 28 + d

    for t in terms:
        k, v = map(str, t.split())
        dict[k] = int(v) * 28

    for i, p in enumerate(privacies):
        date, term = map(str, p.split())
        y, m, d = map(int, date.split('.'))
        valid = y * 12 * 28 + m * 28 + d + dict[term]
        
        if valid <= now:
            answer.append(i + 1)
    
    return answer