N, M = map(int, input().split())

words = []
for i in range(N):
    word = input()
    words.append(word)

count = 0
for j in range(M):
    word = input()
    if word in words:
        count += 1

print(count)