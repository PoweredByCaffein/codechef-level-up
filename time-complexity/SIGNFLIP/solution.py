T = int(input())
for z in range(T):
    user_input = list(map(int, input().split()))
    n = user_input[0]
    k = user_input[1]

    nums = list(map(int, input().split()))
    nums.sort()

    result = 0
    for i in range(n):
        if nums[i] < 0 and k > 0:
            result += (-1 * nums[i])
            k -= 1
        elif nums[i] > 0:
            result += nums[i]

    print(result)
