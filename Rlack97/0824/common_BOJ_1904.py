N = int(input())

# 재귀
# def count(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     else:
#         return count(n-1) + count(n-2)
# 재귀 깊이가 1000이 넘어가 RecursionError가 발생

# 리스트에 저장
# list = [1,2]
# for i in range(3,N+1):
#     value = list[i-3] + list[i-2]
#     list.append(value)
# C = list.pop()
# 메모리 초과 발생

# 변수에 저장 
# a = 1
# b = 2
# for i in range(3,N+1):
#     a, b = b, a+b
# 시간 초과 발생


list = [0,1,2]
for i in range(3,N+1):
    value = (list[i-2] + list[i-1]) % 15746 # 계속 나머지를 구하는 것으로 메모리 확보
    list.append(value) 

print(list[N])
# pop으로 뽑으려고 했으나, N이 2 이하면 값이 달라져버림.