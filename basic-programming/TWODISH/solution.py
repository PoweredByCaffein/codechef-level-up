T = int(input())

for i in range(T):
    user_input = input().split()
    N = int(user_input[0])
    A = int(user_input[1])
    B = int(user_input[2])
    C = int(user_input[3])

    if B >= N and A+C >= N:
        print("YES")
    else:
        print("NO")