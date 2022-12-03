T = int(input())
for i in range(T):
    n = int(input())
    problems = list(map(int, input().split()))

    total_sum = 28
    problems_solved = 0
    for x in range(n):
        if problems[x] <= 7:
            total_sum -= problems[x]
        if total_sum == 0:
            problems_solved = x + 1
            break
    print(problems_solved)
