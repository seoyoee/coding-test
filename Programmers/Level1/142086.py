def solution(s):
    letter = {}
    answer = []
    
    for i in range(len(s)):
        if s[i] in letter:
            answer.append(i - letter[s[i]])
        else:
            answer.append(-1)
        letter[s[i]] = i
    
    return answer