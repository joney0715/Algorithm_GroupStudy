N = int(input())
nums = list(map(int, input().split()))

answer_1 = []
count_1 = 1
for i in range(1, N):
    if nums[i-1] <= nums[i]:
        count_1 += 1
    else:
        answer_1.append(count_1)
        count_1 = 1
answer_1.append(count_1)

answer_2 = []    
count_2 = 1   
for i in range(1, N):
    if nums[i-1] >= nums[i]:
        count_2 += 1
    else:
        answer_2.append(count_2)
        count_2 = 1
answer_2.append(count_2)

print(max(max(answer_1),max(answer_2)))