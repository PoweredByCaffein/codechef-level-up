T = int(input())
for i in range(T):
    user_input = int(input())
    x = user_input % 4
    
    if x == 3 or x == 0:
        print(user_input)
        continue
    
    print(user_input - 1)