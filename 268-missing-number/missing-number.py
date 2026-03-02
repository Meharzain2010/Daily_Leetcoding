class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums = [9,6,4,2,3,5,7,0,1]
        n = len(nums)
        # max_num = max(nums)
        total_sum = n * (n + 1) // 2
        arr_sum = sum(nums) 
        return total_sum - arr_sum
        