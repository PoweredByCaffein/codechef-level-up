T = int(input())
for z in range(T):
    user_input = input().split()
    n = int(user_input[0])
    x = int(user_input[1])

    chocolates = input().split()
    unique_flavors = set(chocolates)

    x -= (n - len(unique_flavors))
    if x <= 0:
        print(len(unique_flavors))
        continue

    print(len(unique_flavors) - x)
