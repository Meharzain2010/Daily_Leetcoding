class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = [] #n = 234
        while n > 0:
            a = n % 10
            lst.append(a)
            n = n // 10
        
        return prod(lst) - sum(lst)
       
class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        sum = 0
        product = 1

        while n > 0:

            digit = n % 10

            sum += digit
            product *= digit

            n //= 10
        
        return product - sum    
        
      
        
        



        
        
        