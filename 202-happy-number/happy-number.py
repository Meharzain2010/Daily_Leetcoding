class Solution:
    def isHappy(self, n: int) -> bool:
        # seen = set()        # n = 19
        
        # while n != 1 and n not in seen:
        #     seen.add(n)
        #     sum_sqr_digits = 0
        #     while n > 0:
        #         sum_sqr_digits += (n % 10) ** 2 # 19 / 10 = 1
        #         n = n // 10 #0
        #     n = sum_sqr_digits
        
        # return n == 1
        
# class Solution(object):
    # def isHappy(self, n):
        seen = []
        while n != 1 and n not in seen:
            seen.append(n)
            n = sum(int(digit) * int(digit) for digit in str(n))   
        return n == 1