class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        # 만약 한 개 남으면, 그대로 리턴.
        if len(nums) == 1:
            return nums[0]

        # 눈 여겨 봐야할 부분은 분할을 통해 재귀를 만드는 이 부분!
        # 슬라이싱을 통해 2개로 쪼개서 재귀하는 알고리즘은 매우 유용하다.
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]