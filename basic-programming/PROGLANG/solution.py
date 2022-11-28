T = int(input())

for i in range(T):
    user_input = input().split()
    A = int(user_input[0])
    B = int(user_input[1])
    C = int(user_input[2])
    D = int(user_input[3])
    E = int(user_input[4])
    F = int(user_input[5])

    if (A == C or A == D) and (B == C or B == D):
        print(1)
    elif (A == E or A == F) and (B == E or B == F):
        print(2)
    else:
        print(0)