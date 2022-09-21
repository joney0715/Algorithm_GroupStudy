class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

    # 파이써닉이 정확히 뭔지는 아직도 모르겠으나 아이디어가 웃기다.