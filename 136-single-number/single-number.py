class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = Counter(nums)   # Count Numbers
        for i in k:
            if k[i] == 1:
                return i 
