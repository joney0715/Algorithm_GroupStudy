
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

flag = 0
for i in range(len(gas)):
    if gas[i] >= cost[i]:
        answer = i
        remain = gas[i] - cost[i]

        idx = i
        while True:
            idx = (idx + 1) % len(gas)
            if idx == answer:
                flag = 1
                break

            remain = remain + gas[idx] - cost[idx]
            if remain < 0:
                answer = -1
                break

    else:
        answer = -1

    if flag:
        break
    
print(answer)
