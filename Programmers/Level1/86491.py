def solution(sizes):
    w = 0
    h = 0
    
    for size in sizes:
        w = max(w, max(size))
        h = max(h, min(size))
    
    return w * h

    # 한 줄 코드
    # return max([max(size) for size in sizes]) * max([min(size) for size in sizes])