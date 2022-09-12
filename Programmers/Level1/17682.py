def solution(dartResult):
    bonus = ['S', 'D', 'T']
    score = []
    
    dart = dartResult.replace('10', 'X')
    
    for i in dart:
        if i == '*':
            score[-1] *= 2
            try:
                score[-2] *= 2
            except:
                pass
        elif i == '#':
            score[-1] *= (-1)
        elif i in bonus:
            score[-1] = score[-1] ** (bonus.index(i)+1)
        elif i == 'X':
            score.append(10)
        else:
            score.append(int(i))
        
    return sum(score)