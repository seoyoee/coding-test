def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x : (x[col - 1], -x[0]))
    
    for i in range(row_begin, row_end + 1):
        sum = 0
        for num in data[i - 1]:
            sum += num % i
        answer ^= sum
    
    return answer