
N = int(input())

N_list = [0]
for _ in range(N):
    n = int(input())
    N_list.append(n)

max_value = 0
answer = 0
for i in range(1,N+1):
    a = b = i
    visit = [False] * (N+1)
    visit[a] = True

    cnt = 0
    j = N_list[a]
    while True:
        if visit[j]:
            break
        visit[j] = True
        cnt += 1
        a = j
        j = N_list[j]

    if max_value < cnt:
        max_value = cnt
        answer = b

print(answer)


