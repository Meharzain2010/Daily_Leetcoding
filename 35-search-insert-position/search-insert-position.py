class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index if 
        the target is found. If not, return the index where it would be if it were 
        inserted in order.
        -------------------------------------------------------------------------
        You must write an algorithm with O(log n) runtime complexity.
        Example 1:
        Input: nums = [1,3,5,6], target = 5
        Output: 2
        
        Example 2:
        Input: nums = [1,3,5,6], target = 2
        Output: 1
        
        Example 3:
        Input: nums = [1,3,5,6], target = 7
        Output: 4
        """  
        
                            # nums = [1,3,5,6], target = 7                            
        l = 0   #1 -> 2 -> 3 -> 4
        r = len(nums) - 1   #3
        
            
        while l <= r:   # 4 <= 3
            mid  = (l + r) // 2    # 3
            if nums[mid] == target: # 6 == 7 
                return mid
            elif nums[mid] < target: # 6 < 7
                l = mid + 1
            elif nums[mid] > target: #
                r = mid - 1
        
        return l 
                    
        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)): #  # nums = [1,3,5,6], target = 2
            if nums[i] >= target:
                return i
        return len(nums)
                
                

            
        