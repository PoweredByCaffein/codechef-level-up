T = int(input())

for i in range(T):
    inputs = input().split()
    inputs = [int(item) for item in inputs]
    D = inputs[0]
    L = inputs[1]
    R = inputs[2]

    if D >= L and D <= R:
        print("Take second dose now")
    elif D < L:
        print("Too Early")
    else:
        print("Too Late")