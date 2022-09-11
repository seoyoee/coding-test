def solution(a, b):
    month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = {3:'SUN', 4:'MON', 5:'TUE', 6:'WED', 0:'THU', 1:'FRI', 2:'SAT'}
    
    return day[(sum(value for key, value in month.items() if key < a) + b) % 7]