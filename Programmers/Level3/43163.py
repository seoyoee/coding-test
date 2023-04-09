def solution(begin, target, words):
    stack = [begin]
    step = {begin : 0}
    
    while stack:
        now = stack.pop()
        
        if now == target:
            return step[now]
        
        for word in words:
            if word not in step:
                count = 0
                for i in range(len(now)):
                    if now[i] != word[i]:
                        count += 1
                        
                if count == 1:
                    stack.append(word)
                    step[word] = step[now] + 1
        
    return 0