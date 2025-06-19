class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = []
        for num in nums:
            num = num ** 2
            square.append(num)
        return sorted (square)