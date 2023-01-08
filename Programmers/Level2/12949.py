def solution(arr1, arr2):
    answer = []
    arr2 = list(zip(*arr2))
    
    for row in arr1:
        arr3 = []
        for col in arr2:
            sum = 0
            for i in range(len(row)):
                sum += row[i] * col[i]
            arr3.append(sum)
        answer.append(arr3)
    
    return answer