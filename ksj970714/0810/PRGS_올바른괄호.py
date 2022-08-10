def solution(s):
    b = []
    for i in s:
        if i == '(':
            b.append(i)
        else:
            try:
                b.pop()
            except IndexError:
                return False
                break
    if b == []:
        return True
    else:
        return False