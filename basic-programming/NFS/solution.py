import math

T = int(input())
for i in range(T):
    user_input = input().split()
    U = int(user_input[0])
    V = int(user_input[1])
    A = int(user_input[2])
    S = int(user_input[3])
    
    if U <= V:
        print("Yes")
        continue
    
    temp = (U*U)-(2*A*S)
    if temp <= 0:
        print("Yes")
        continue
    
    min_velocity = math.sqrt(temp)
    
    if min_velocity <= V:
        print("Yes")
    else:
        print("No")