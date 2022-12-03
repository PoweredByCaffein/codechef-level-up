T = int(input())
for z in range(T):
    user_input = list(map(int, input().split()))
    N = user_input[0]
    K = user_input[1]

    measurements = list(map(int, input().split()))
    measurements.sort()

    if K != 0:
        measurements = measurements[K:N]
        measurements = measurements[0:-1 * K]

    avg = 0
    for measurement in measurements:
        avg += measurement

    print(avg / len(measurements))
