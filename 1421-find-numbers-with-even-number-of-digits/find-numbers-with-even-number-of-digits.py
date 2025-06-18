class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:    # nums = [12,345,2,6,7896]
            # num = str (num)
            if len(str(num)) % 2 == 0 :
                count += 1
        return count

            