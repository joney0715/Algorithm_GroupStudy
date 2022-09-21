class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums)//2: #갯수 세 주는 메서드:
                return num