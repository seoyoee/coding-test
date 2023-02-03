import sys

n, m = map(int, sys.stdin.readline().split())

pokemon_name = {}
pokemon_num = {}

for i in range(n):
    pokemon = sys.stdin.readline().strip()
    pokemon_name[pokemon] = i + 1
    pokemon_num[i + 1] = pokemon

for i in range(m):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(pokemon_num[int(question)])
    else:
        print(pokemon_name[question])