T = int(input())
for t in range(T):
    length = int(input())
    elements = list(map(int, input().split()))
    maximum = 0

    for i in range(1, length):
        temp = elements.count(elements[i])
        if temp > maximum:
            maximum = temp
    if maximum == 0:
        print(0)
        continue

    print(length - maximum)
