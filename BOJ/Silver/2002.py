n = int(input())

car_in = []
car_out = []
answer = 0

for i in range(n):
    car_in.append(input())
for i in range(n):
    car_out.append(input())

for i in range(n):
    for j in range(i+1, n):
        if car_in.index(car_out[i]) > car_in.index(car_out[j]):
            answer += 1
            break

print(answer)