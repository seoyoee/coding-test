import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    
    for score in scoville:
        heapq.heappush(heap, score)
    
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first + second * 2)
        answer += 1
    
    return answer