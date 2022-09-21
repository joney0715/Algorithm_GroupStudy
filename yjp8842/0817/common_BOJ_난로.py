N, K = map(int, input().split())
time_list = []  # 친구들이 오는 시간
time_table = [] # 시간 사이의 간격

for _ in range(N):
    time_list.append(int(input())) # 오는 시간 입력값 받기

for i in range(len(time_list) - 1): # 시간 간격값 새로운 배열에 append
    time_table.append(time_list[i + 1] - time_list[i])
    
time_table = sorted(time_table)  # 시간 간격 오름차순으로 정렬

for _ in range(K - 1):
    time_table.pop()   # 가장 큰 원소 K - 1번 pop
    
for _ in range(K):
    time_table.append(1) # K개 만큼 1을 append

print(sum(time_table)) # 리스트의 합을 출력