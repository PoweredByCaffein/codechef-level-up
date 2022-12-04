T = int(input())
for z in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    output = "YES"

    for i in range(n - 1):
        if nums[i + 1] - nums[i] > 1:
            output = "NO"
            break

    print(output)
