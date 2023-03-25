import heapq

def solution(n, k, enemy):
    
    if len(enemy) <= k:
        return len(enemy)
    
    heap = []
    sum = 0
    for i in range(len(enemy)):
        if len(heap) < k:
            heapq.heappush(heap, enemy[i])
        elif heap[0] < enemy[i]:
            sum += heapq.heappop(heap)
            heapq.heappush(heap, enemy[i])
        else:
            sum += enemy[i]
            
        if sum <= n:
            answer = i + 1
        else:
            break
        
    return answer