T = int(input())

for i in range(T):
    inputStr = input().split()
    inputStr = [int(item) for item in inputStr]
    A = inputStr[0]
    B = inputStr[1]
    X = inputStr[2]
    
    diff = B - A

    if diff % X == 0:
        print(int(diff/X))
    else:
        print(int(diff/X) + 1)
