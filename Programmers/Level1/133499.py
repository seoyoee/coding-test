def solution(babbling):
    nephew = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for word in babbling:
        prev = ""
        while word:
            if word[:3] in nephew and word[:3] != prev:
                prev = word[:3]
                word = word[3:]
            elif word[:2] in nephew and word[:2] != prev:
                prev = word[:2]
                word = word[2:]
            else:
                break
        
        if not len(word):
            count += 1
    
    return count