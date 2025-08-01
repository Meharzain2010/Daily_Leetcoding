#Method 1
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        nums1 = set(nums1)  
        nums2 = set(nums2)  

        for num in nums1:
            if num in nums2:
                answer.append(num)
                

        return answer

# Method 2
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result =[]        
        for num in nums1:  
            if num in nums2 and num not in result:
                result.append(num)
        return result


# 3 Method
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))


