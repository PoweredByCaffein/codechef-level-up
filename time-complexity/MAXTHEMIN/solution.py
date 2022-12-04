T = int(input())
for z in range(T):
    user_input = list(map(int, input().split()))
    N, K = user_input[0], user_input[1]
    nums = list(map(int, input().split()))

    nums.sort()

    if K >= N - 1:
        print(nums[N - 1])
        continue

    nums = nums[K:N]

    print(nums[0])
