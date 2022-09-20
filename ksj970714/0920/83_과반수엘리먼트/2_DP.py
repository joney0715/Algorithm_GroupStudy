import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] ==0:
                counts[num] = nums.count(num)
            if counts[num] > len(nums)//2: #갯수 세 주는 메서드:
                return num

# 우리가 흔히 활용하는 이 방법도, 같은 연산을 두번 반복하지 않게 해준다는 점에서
# DP라고 하네요.