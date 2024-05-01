string = input().split()
near = set()
while string != []:
    for i in range(len(string)):
        if string[i] == 'зайка':
            if i == 0:
                near.add(string[i + 1])
            elif i == len(string) - 1:
                near.add(string[i - 1])
            else:
                near.add(string[i - 1])
                near.add(string[i + 1])
    string = input().split()

for el in near:
    print(el)
