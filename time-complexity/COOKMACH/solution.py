import math

T = int(input())
for z in range(T):
    user_input = list(map(int, input().split()))
    A, B = user_input[0], user_input[1]

    operations = 0
    # A != 1 is introduced to ensure that the value of A doesn't become 0 after this if block
    if A % 2 != 0 and A != 1:
        operations += 1
        A = int((A-1)/2)

    power_a = int(math.log10(A) / math.log10(2))
    power_b = int(math.log10(B) / math.log10(2))

    print(max(power_a-power_b, power_b-power_a) + operations)

