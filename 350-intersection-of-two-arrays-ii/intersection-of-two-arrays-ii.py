class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 = [4,9,9,5], nums2 = [9,4,9,8,4]
        result =[]        
        for num in nums1:  
            if num in nums2:
                nums2.remove(num)
                result.append(num)
        return result