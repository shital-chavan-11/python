numbers = input("Enter binary numbers separated by commas: ").split(',')
for i in numbers:
    if int(i, 2) % 5 == 0:
        print(i)  