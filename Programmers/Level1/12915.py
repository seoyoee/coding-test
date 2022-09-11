def solution(strings, n):
    lists = sorted(zip([string[n] for string in strings], strings))
    return [j for i, j in lists]