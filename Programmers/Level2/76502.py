def solution(s):
    answer = 0
    brace = {"(": ")", "[": "]", "{": "}"}
    
    for i in range(len(s)):
        stack = []
        rotate = s[i:] + s[:i]
        
        for r in rotate:
            if r in brace.keys():
                stack.append(r)
            elif stack and brace[stack[-1]] == r:
                stack.pop()
            else:
                stack.append(r)
                break
                
        if not stack:
            answer += 1
    
    return answer