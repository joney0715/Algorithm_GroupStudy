class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if expression.isdigit():  # 만약에 숫자라면,
            return [int(expression)]
        '''
        부호를 만나면 좌우분할 후 계산 결과 리턴.
        예를들면 이런식이다. 1-2+3*4인 경우
        ㄴ(는 재귀안에 들어간 표시)
        1 - (2+3*4)
        ㄴ 1 - 2 +(3*4)
        ㄴ 1 - (2+3) * 4
        ㄴ return
        -
        1-2 + (3*4)
        ㄴ (1-2) (3*4)
        ㄴ return
        (1-2+3) * 4
        ㄴ (1-2) + 3 * 4
        ㄴ 1 - (2+3) * 4
        ㄴ return

        이런식으로 5개의 식을 계산 가능하다.
        '''
        results = []
        for index, value in enumerate(expression):
            if value in "-+*":  # 이것도 참고할 만 하다.
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])  # 좌우분할재귀
                # right의 index+1인 이유는 계산 기호는 제거해야 하니까
                results.extend(compute(left, right, value))  # 리스트에 리스트를 더하기 위함
        return results


