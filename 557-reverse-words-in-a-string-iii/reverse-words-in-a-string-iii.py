class Solution:
    def reverseWords(self, s: str) -> str:
        #s = "Let's take LeetCode contest"
        s = s.split()
        ans = []
        for i in s:
            i = list(i)
            
            
            # Two pointer approch
            
            l = 0
            r = len(i) -1
            while l < r:
                i[l], i[r] = i[r],i[l]
                l += 1
                r -= 1
            i = "".join(i)
            ans.append(i)

        ans = " ".join(ans)
        return ans

        