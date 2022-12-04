T = int(input())
for z in range(T):
    user_input = list(map(float, input().split()))
    N = user_input[0]
    K = user_input[1]

    gifts = list(map(float, input().split()))
    gifts.sort()

    gifts_brought = 0
    coupon_used = False

    for gift in gifts:
        if gift <= K:
            gifts_brought += 1
            K -= gift
        elif (gift / 2) <= K and not coupon_used:
            gifts_brought += 1
            K -= gift / 2
            coupon_used = False

    print(gifts_brought)
