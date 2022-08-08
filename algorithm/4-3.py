# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

count = 0

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
for step in steps:
    if 1 <= row + steps[0] <= 8 and 1 <= col + steps[1] <= 8:
        count += 1

print(count)