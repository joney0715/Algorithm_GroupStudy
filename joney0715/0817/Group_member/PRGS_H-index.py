def solution(citations):
    # 레퍼런스 수
    for ref in range(10000):
        count = 0
        # 논문 중 레퍼런스된 수
        for i in citations:
            # 레퍼런스 수를 달성한 논문 수
            if ref <= i:
                count += 1
        
        # 논문 수가 미달인 경우 연산 종료
        if ref >= count:
            break
            
    return count