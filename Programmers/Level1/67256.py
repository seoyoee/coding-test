def solution(numbers, hand):    
    lh = [1, 4, 7]
    rh = [3, 6, 9]
    curl = [3, 0]
    curr = [3, 2]
    
    answer = ''
    
    for num in numbers:
        if num:
            loc = [(num-1)//3, (num-1)%3]
        else:
            loc = [3, 1]
        
        if num in lh:
            answer += 'L'
            curl = loc
        elif num in rh:
            answer += 'R'
            curr = loc
        
        else:
            l = abs(loc[0] - curl[0]) + abs(loc[1] - curl[1])
            r = abs(loc[0] - curr[0]) + abs(loc[1] - curr[1])
            if l < r or (l == r and hand == 'left'):
                answer += 'L'
                curl = loc
            elif l > r or (l == r and hand == 'right'):
                answer += 'R'
                curr = loc
                    
    return answer