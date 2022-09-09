def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += i
        elif i.isupper() and ord(i) + n > ord('Z'):
            answer += chr(ord(i) + n - 26)
        elif i.islower() and ord(i) + n > ord('z'):
            answer += chr(ord(i) + n - 26)
        else:
            answer += chr(ord(i) + n)
    
    return answer