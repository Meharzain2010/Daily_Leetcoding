class Solution:
    def maximumProduct(self, nums: List[int]) -> int:  #nums = [-2,-100,-1,2,3,4]
        nums.sort()     # [-100,1,2,3,4]       
        product_1 = nums[-1] * nums[-2] * nums[-3]    #24
        product_2= nums[0] * nums[1] * nums[-1]      #-400
        return max(product_1,product_2)

       

        