#교재 풀이

def isBalanced(root):
    def check(root):
        # 루트가 아니라면
        if not root:
            return 0

        left = check(root.left)
        right = check(root.right)

        # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    return check(root) != -1


root = [3, 9, 10, None, None, 15, 7]