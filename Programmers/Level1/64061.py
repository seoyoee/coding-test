def solution(board, moves):
    A = [list(x) for x in zip(*board)]
    basket = []
    answer = 0
    
    for i in moves:
        for j in range(len(A)):
            if A[i-1][j]:
                basket.append(A[i-1][j])
                A[i-1][j] = 0
                
                if len(basket) >= 2:
                    if basket[-1] == basket[-2]:
                        del basket[-2:]
                        answer += 2
                break
        
    return answer