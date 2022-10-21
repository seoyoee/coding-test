def solution(s):
    answer = ''
    index = 1
    
    for i in list(s):
        if i == ' ':
            answer += i
            index = 1
        elif index % 2:
            answer += i.upper()
            index += 1
        else:
            answer += i.lower()
            index += 1
    
    return answer