def solution(s):
    while True:
        # ()쌍이 있으면 삭제
        if s.find('()') != -1:
            s = s.replace('()', '')
        # 없으면 중단
        else:
            break
    if s:
        return False
    else:
        return True