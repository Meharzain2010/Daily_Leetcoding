class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}    # {4:1 , 1:2 , 2:2 }
        for i in nums:  #nums = [4,1,2,1,2]

            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        for i in dic:
            if dic[i] == 1:
                return i

                                # (Alternative Method)


#         k = Counter(nums)   
#         for i in k:         
#             if k[i] == 1:
#                 return i 