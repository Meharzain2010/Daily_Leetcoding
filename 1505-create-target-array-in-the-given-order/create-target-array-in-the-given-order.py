class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

                                # nums = [0,1,2,3,4,5], index = [0,1,2,2,1,4]
        target_array = []
        for i in range(len(nums)): 
            target_array.insert(index[i],nums[i])
        return target_array




