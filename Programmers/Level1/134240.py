def solution(food):
    result = ''
    
    for i in range(len(food)):
        result += str(i) * (food[i] // 2)
        
    result += '0' + result[::-1]
    return result