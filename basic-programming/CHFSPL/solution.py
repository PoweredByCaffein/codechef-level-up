T = int(input())

for i in range(T):
    user_input = input().split()
    A = int(user_input[0])
    B = int(user_input[1])
    C = int(user_input[2])

    sum = A + B + C
    min = A

    if min > B:
        min = B
    
    if min > C:
        min = C
    
    print(int(sum - min))