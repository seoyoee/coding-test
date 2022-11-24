def solution(brown, yellow):
    all = brown + yellow
    arr = [x for x in range(2, all) if not all % x]
    for height in arr:
        width = all / height
        if (height - 2) * (width - 2) == yellow:
            return [width, height]