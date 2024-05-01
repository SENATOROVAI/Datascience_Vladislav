def odd_and_even(number):
    even = len([x for x in str(number) if int(x) % 2 == 0])
    odd = len([x for x in str(number) if int(x) % 2 != 0])
    if even > odd:
        return 1
    elif even < odd:
        return 0
    else:
        return -1


file_input = input()
file_even = input()
file_odd = input()
file_eq = input()
count_even = 0
count_odd = 0
with open(file_input, encoding="UTF-8") as file_1:
    numbers = []
    for line in file_1:
        start = list(map(int, line.strip().split()))
        for number in start:
            if odd_and_even(number) == 1:
                with open(file_even, "a", encoding="UTF-8") as file_2:
                    print(number, end=' ', file=file_2)
            elif odd_and_even(number) == 0:
                with open(file_odd, "a", encoding="UTF-8") as file_3:
                    print(number, end=' ', file=file_3)
            elif odd_and_even(number) == -1:
                with open(file_eq, "a", encoding="UTF-8") as file_4:
                    print(number, end=' ', file=file_4)
        with open(file_even, "a", encoding="UTF-8") as file_2:
            print('\n', end='', file=file_2)
        with open(file_odd, "a", encoding="UTF-8") as file_3:
            print('\n', end='', file=file_3)
        with open(file_eq, "a", encoding="UTF-8") as file_4:
            print('\n', end='', file=file_4)
