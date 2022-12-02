T = int(input())

for i in range(T):
    matches_count = {
        0 : 6,
        1 : 2,
        2 : 5,
        3 : 5, 
        4 : 4,
        5 : 5,
        6 : 6,
        7 : 3,
        8 : 7,
        9 : 6,
    }
    
    
    user_input = input().split()
    A = int(user_input[0])
    B = int(user_input[1])
    
    sum = A + B
    result = 0
    while sum != 0:
        temp = sum % 10
        result += matches_count.get(temp, 0)
        sum = int(sum/10)
 
    print(result)