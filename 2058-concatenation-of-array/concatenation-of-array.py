class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
                            #Easy
            
        return nums + nums

                            # Medium

        ans = []
        for i in range(2):
            for i in nums:
                ans.append(i)
        return ans



                            #Hard


        ans = []
        n = len(nums) * 2
        for i in range(n):
            ans.append([i % len (nums)] )
        return ans







