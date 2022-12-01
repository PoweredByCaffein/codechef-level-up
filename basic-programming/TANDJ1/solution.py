T = int(input())
for i in range(T):
    user_input = input().split()
    a = int(user_input[0])
    b = int(user_input[1])
    c = int(user_input[2])
    d = int(user_input[3])
    K = int(user_input[4])
    
    x = c - a 
    y = d - b

    if x < 0:
        x *= -1
    if y < 0:
        y *= -1
    
    distance = x + y

    if K < distance:
        print("NO")
        continue

    if (K - distance) % 2 == 0:
        print("YES")
    else:
        print("NO")

