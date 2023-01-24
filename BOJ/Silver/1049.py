n, m = map(int, input().split())

package, each = map(int, input().split())
for i in range(m-1):
    a, b = map(int, input().split())
    package = min(package, a)
    each = min(each, b)

case1 = package * (n // 6) + each * (n % 6)
case2 = package * ((n - 1) // 6 + 1)
case3 = each * n
print(min(case1, case2, case3))