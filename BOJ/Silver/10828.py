import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    func = sys.stdin.readline().rstrip()

    if "push" in func:
        stack.append(int(func[5:]))
    elif func == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif func == "size":
        print(len(stack))
    elif func == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif func == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)