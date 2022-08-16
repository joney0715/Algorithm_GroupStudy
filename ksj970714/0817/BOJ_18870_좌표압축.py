N = int(input())
numbers = list(map(int,input().split()))
set_numbers = list(set(numbers))
set_numbers.sort()
mydict = {}
dummy=[]
for i in range(len(set_numbers)):
    mydict[set_numbers[i]]=i

for number in numbers:
    dummy.append(mydict[number])

print(*dummy)