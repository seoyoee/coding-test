a = int(input())
b = str(input())

for i in reversed(range(3)):
    print(a * int(b[i]))
print(a * int(b))