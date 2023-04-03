def solution(name, yearning, photo):
    answer = []
    
    for row in photo:
        result = 0
        for person in row:
            if person in name:
                result += yearning[name.index(person)]
        answer.append(result)
    
    return answer