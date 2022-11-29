def solution(people, limit):
    people.sort(reverse=True)
    boat = 0
    
    for person in people:
        if person + people[-1] <= limit:
            del people[-1]
        boat += 1
    
    return boat