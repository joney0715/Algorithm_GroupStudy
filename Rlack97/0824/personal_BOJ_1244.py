N = int(input())
switch = [99] + (list(map(int,input().split())))
S = int(input())

def control(value):
    if value == 0:
        return 1
    elif value == 1:
        return 0

for s in range(S):
    sex, num = map(int,input().split())

    if sex == 1:
        for n in range(1,N+1):  # index 
            if n % num == 0:
                switch[n] = control(switch[n])
    else:
        switch[num] = control(switch[num])
        i = 1
        while num+i <= N and num-i >= 0:
            if switch[num+i] == switch[num-i]:
                switch[num+i] = control(switch[num+i])
                switch[num-i] = control(switch[num-i]) 
                i += 1
            else:
                break


for r in range(1,N+1):
    print(switch[r], end = " ")
    if r%20 == 0:
        print()
