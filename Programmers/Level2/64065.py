from collections import defaultdict

def solution(s):
    
    count = defaultdict(int)
    tuple = ''
    
    for c in s:
        if c == '{':
            continue
        elif c in ['}', ',']:
            if tuple != '':
                count[int(tuple)] += 1
                tuple = ''
            else:
                continue
        else:
            tuple += c
    
    return sorted(count, key=lambda x:count[x], reverse=True)