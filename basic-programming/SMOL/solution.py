T = int(input())
for i in range(T):
    user_input = input().split()
    N = int(user_input[0])
    K = int(user_input[1])
    
    if K == 0:
        print(N)
        continue
    
    print(N%K)