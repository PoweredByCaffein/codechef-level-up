T = int(input())

for i in range(T):
    user_input = input().split()
    N = int(user_input[0])
    X = int(user_input[1])

    max_rating = 0
    for j in range(N):
        user_input = input().split()
        if int(user_input[0]) <= X:
            if int(user_input[1]) > max_rating:
                max_rating = int(user_input[1])

    print(max_rating)
