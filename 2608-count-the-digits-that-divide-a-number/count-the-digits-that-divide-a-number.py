class Solution:
    def countDigits(self, num: int) -> int:
        nums = str(num)
        count = 0       
        for n in nums:#1
            if int(nums) % int(n) == 0:
                count += 1
        return count
        
        
        
        
        # n = "1234"