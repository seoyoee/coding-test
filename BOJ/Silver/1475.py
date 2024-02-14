num = input()
dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for n in num:
    if n not in dict:
        dict[n] = 1
    elif n in ['6', '9']:
        if dict['6'] > dict['9']:
            dict['9'] += 1
        else:
            dict['6'] += 1
    else:
        dict[n] += 1

print(max(dict.values()))