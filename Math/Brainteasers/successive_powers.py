a = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
even = []
check = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        continue

for int in even:
    for i in a:
        for z in range(1, 11):
            if (i * z - int) == 1:
                print(int, i)
