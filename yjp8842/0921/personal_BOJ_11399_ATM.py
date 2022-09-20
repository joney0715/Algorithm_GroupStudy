N = int(input())
time = list(map(int, input().split()))

# 오름차순으로 정렬
time.sort()
# 리스트 초기화
times = [0]
for num in time:
    # times = [0, 1, 3, 6, 9, 13]
    times.append(num + times[-1])
    
print(sum(times))