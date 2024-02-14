string = input()
flag = 0
stack = []
answer = ''

for s in string:
    if not flag:
        if s == '<':
            stack.reverse()
            answer += ''.join(stack)
            answer += s
            stack = []
            flag = 1
        elif s == ' ':
            stack.reverse()
            answer += ''.join(stack)
            answer += s
            stack = []
        else:
            stack.append(s)
    
    elif flag:
        if s == '>':
            answer += s
            flag = 0
        else:
            answer += s

if stack:
    stack.reverse()
    answer += ''.join(stack)

print(answer)