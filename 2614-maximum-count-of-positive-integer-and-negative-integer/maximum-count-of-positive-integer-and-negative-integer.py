class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0 
        neg = 0
        
        for num in nums: 
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1
        return max(pos,neg)
        
        
        # if pos >= neg:
        #     return pos
        # elif pos < neg:
        #     return neg
        # elif pos == neg:
        #     return pos
        
        
        
        
        
        
        
        
        # pos = [1,1,1,2,3]
        # neg = [-2,-1,-1]
        # # nums = [-2,-1,-1,0,1,1,1,2,3]
        # pos_len = len(pos)
        # neg_len = len(neg)
