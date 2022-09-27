def cut(number):
    n = N // 4
    return [int(number[0:n], 16), int(number[n:2*n], 16), int(number[2*n:3*n], 16), int(number[3*n:4*n], 16)]

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    num = input()

    num_list = cut(num)
    for i in range(1, N):
        num = list(num)
        k = num[0]
        for j in range(1, N):
            num[j-1] = num[j]
        num[N-1] = k
        num = ''.join(num)

        num_list.extend(cut(num))

    num_list = set(num_list)

    num_list = sorted(num_list, reverse=True)

    print('#{}'.format(tc), num_list[K-1])