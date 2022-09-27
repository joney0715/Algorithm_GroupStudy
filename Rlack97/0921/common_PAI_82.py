# 82_쿠키부여  풀이
# 2022-09-17

# 자체풀이 (백준식)

childs = list(map(int,input().split()))
cookies = list(map(int,input().split()))

# 아이들의 그리드 팩터와 쿠키들의 크기를 입력받는다.
cnt = 0

childs.sort()
cookies.sort()
i,j = 0,0

while i < len(childs) and j < len(cookies):
    if childs[i] <= cookies[j]:
        # 쿠키 크기를 만족하면
        cnt += 1
        i += 1
        j += 1
        # 다음 아이의 값으로 넘어가면서, 다음 쿠키값을 사용
    else:
        j += 1
        # 다른 쿠키를 본다

    # while문에서 벗어나는 순간, 
    # 남아있는 아이들 중 가장 작은 값을 지닌 아이의 그리드값을 만족하는 쿠키가 없다는 뜻이므로
    # 나머지 아이들도 볼 필요가 없음.
print(cnt)


# 교재풀이 1 (리트코드식) 그리디
def FindChildren(self, g, s):
    g.sort() 
    # 아이들의 그리드 값 리스트

    s.sort()
    # 쿠키 사이즈 리스트

    child_i = cookie_j = 0
    # 사용할 인덱스 정의

    while child_i < len(g) and cookie_j < len(s):
        # 인덱스 에러를 방지하기 위한 구문

        if s[cookie_j] >= g[child_i]:
            # 값을 만족한다면

            child_i += 1
            # 다음 아이를 본다

        cookie_j += 1
        # 만족하지 않으면 쿠키를 본다

    return child_i
    # while을 그만두는 시점에서의 아이의 인덱스가 곧 만족한 아이의 수.


# 교재풀이 2 이진검색

def FindChildren2(self, g, s):
    g.sort()
    s.sort()
    result = 0
    for i in s:
        index = bisect.bisect_right(g,i)
            # 아이들 리스트 내부에서 i값, 즉 쿠키 사이즈 값을 이진탐색
            # bisect_right는 찾아낸 값의 인덱스에 +1을 해서 반환한다. 
            # 즉, 해당 쿠키값보다 작은 그리드값을 가진 아이들의 수.
        if index > result:
            # 인덱스값이 현재 쿠키를 준 아이의 값보다 클 경우 더 줄 수 있음.
            result += 1
    return result