T = int(input())

for i in range(T):
    user_input = input().split()
    S = int(user_input[0])
    A = int(user_input[1])
    B = int(user_input[2])
    C = int(user_input[3])
    
    new_price = S + ((C/100)*S)
    
    if A <= new_price <= B:
        print("Yes")
    else:
        print("No")