# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
a, b, c = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 좌표 방문 처리
d[a][b] = 1

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방문한 칸의 수
count = 1
# 회전 횟수
turn_time = 0

# 시뮬레이션 시작
while True:
    # 왼쪽으로 회전
    if c == 0:
        c = 3
    else:
        c -= 1
    turn_time += 1

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    x = a + dx[c]
    y = b + dy[c]

    if d[x][y] == 0 and array[x][y] == 0:
        a = x
        b = y
        d[a][b] = 1
        count += 1
        turn_time = 0
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        x = a - dx[c]
        y = b - dy[c]
        # 뒤가 바다로 막혀있지 않으면 이동
        if array[x][y] == 0:
            a = x
            b = y
            turn_time = 0
        # 뒤가 바다로 막혀있는 경우
        else:
            break

print(count)