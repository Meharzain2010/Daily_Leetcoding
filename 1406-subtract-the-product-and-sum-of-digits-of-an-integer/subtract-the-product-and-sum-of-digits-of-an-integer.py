class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = [] #n = 234
        while n > 0:
            a = n % 10
            lst.append(a)
            n = n // 10
        
        ans = prod(lst) - sum(lst)
        return ans
        
        
        
        
        
        



        
        
        