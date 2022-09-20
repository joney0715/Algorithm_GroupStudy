import heapq

N = int(input())

cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

answer = 0
while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    answer += a+b
    heapq.heappush(cards, a+b)

print(answer)

