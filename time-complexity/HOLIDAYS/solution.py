T = int(input())
for i in range(T):
    user_input = list(map(int, input().split()))
    N = user_input[0]
    W = user_input[1]
    days = list(map(int, input().split()))
    days.sort(reverse=True)

    earned = 0
    work_days = 0

    for x in range(N):
        earned += days[x]
        if earned >= W:
            work_days = x + 1
            break

    print(N - work_days)
