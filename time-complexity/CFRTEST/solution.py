T = int(input())

for i in range(T):
    n = int(input())
    party_days = list(map(int, input().split()))
    unique_days = []
    for day in party_days:
        if day not in unique_days:
            unique_days.append(day)

    print(len(unique_days))

