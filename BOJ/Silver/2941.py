word = input()
count = 0

for i in range(len(word)):
    count += 1
    if word[i] == '=':
        if word[i-1] in 'czs':
            count -= 1
            if word[i-1] == 'z' and word[i-2] == 'd':
                count -= 1

    elif word[i] == '-':
        if word[i-1] in 'cd':
            count -= 1
    
    elif word[i] == 'j':
        if word[i-1] in 'ln':
            count -= 1

print(count)