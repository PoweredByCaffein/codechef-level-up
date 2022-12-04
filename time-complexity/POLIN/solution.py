T = int(input())
for z in range(T):
    n = int(input())

    unique_x = []
    unique_y = []

    for y in range(n):
        coordinates = input().split()
        unique_x.append(coordinates[0])
        unique_y.append(coordinates[1])

    print(len(set(unique_y)) + len(set(unique_x)))
