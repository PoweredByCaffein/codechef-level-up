T = int(input())
for i in range(T):
    user_input = input().split()
    w1 = int(user_input[0])
    w2 = int(user_input[1])
    x1 = int(user_input[2])
    x2 = int(user_input[3])
    M = int(user_input[4])
    
    lower_range = w1 + (x1*M)
    upper_range = w1 + (x2*M)
    
    if lower_range <= w2 <= upper_range:
        print(1)
    else:
        print(0)