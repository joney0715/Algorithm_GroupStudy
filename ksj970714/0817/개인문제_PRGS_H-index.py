def solution(citations):

    big = [0] * len(citations)
    dummy = [0]*len(citations)
    for idx in range(len(citations)):
        for idx2 in range(len(citations)):
            if citations[idx] <= citations[idx2]:
                dummy[idx] += 1
    for i in range(len(citations)):
        big[i] = min(dummy[i],citations[i])
    answer = max(big)

    return answer
