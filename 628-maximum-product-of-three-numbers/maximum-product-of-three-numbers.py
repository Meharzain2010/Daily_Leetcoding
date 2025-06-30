class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pos_product = nums[-1] * nums[-2] * nums[-3]
        neg_product = nums[0] * nums[1] * nums[-1]
        return max(pos_product,neg_product)

       

        