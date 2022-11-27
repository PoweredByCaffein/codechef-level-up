T = int(input())

for i in range(T):
    inputs = input().split()
    inputs = [int(item) for item in inputs]
    N = inputs[0]
    S = inputs[1]
   
    if S == N:
        print(N)
    elif S < N:
        print(S)
    else:
        print(N-(S-N))