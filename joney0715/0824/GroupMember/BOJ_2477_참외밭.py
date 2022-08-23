N = int(input())
D = []
for _ in range(6):
    d = list(map(int, input().split()))
    D.append(d[1])

idx = D.index(max(D))
if D[(idx+1)%6] > D[idx-1]:
    D_ = D[(idx+1)%6] * max(D)
    d_ = D[((idx + 3) % 6)] * D[((idx + 4) % 6)]
    answer = (D_ - d_) * N
else:
    D_ = D[idx-1] * max(D)
    d_ = D[((idx + 2) % 6)] * D[((idx + 3) % 6)]
    answer = (D_ - d_) * N

print(answer)
