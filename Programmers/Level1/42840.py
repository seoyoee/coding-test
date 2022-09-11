def solution(answers):
    answer = []
    score = [0] * 3
    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        
    for i in range(len(answers)):
        if answers[i] == st1[i % 5]:
            score[0] += 1
        if answers[i] == st2[i % 8]:
            score[1] += 1
        if answers[i] == st3[i % 10]:
            score[2] += 1
                
    for j in range(3):
        if score[j] == max(score):
            answer.append(j + 1)
    return answer