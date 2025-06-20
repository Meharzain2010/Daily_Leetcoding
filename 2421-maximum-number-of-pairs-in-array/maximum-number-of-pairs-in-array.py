class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        digits = []
        pairs = 0
        for num in nums:
            if num in digits:
                pairs += 1
                digits.remove(num)
            else:
                digits.append(num)
        leftovers = len(digits)
        return [pairs , leftovers]
