def solution(survey, choices):
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    kbti = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    answer = ''
    
    for i in range(len(survey)):
        if choices[i] < 4:
            kbti[survey[i][0]] += score[choices[i]]
        elif choices[i] > 4:
            kbti[survey[i][1]] += score[choices[i]]
    
    if kbti['R'] >= kbti['T']: answer += 'R'
    else: answer += 'T'
    if kbti['C'] >= kbti['F']: answer += 'C'
    else: answer += 'F'
    if kbti['J'] >= kbti['M']: answer += 'J'
    else: answer += 'M'
    if kbti['A'] >= kbti['N']: answer += 'A'
    else: answer += 'N'
    return answer