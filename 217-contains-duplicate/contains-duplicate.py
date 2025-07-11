# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         final = []
#         for num in nums:
#             if num not in final:
#                 final.append(num)
#         if len(final) == len(nums):
#             return False
#         else:
#             return True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

         
        

        
            
     
        

            