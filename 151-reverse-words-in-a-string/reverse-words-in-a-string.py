class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        a = s.split()
        left = 0
        right = len (a) - 1
        while left < right :
            a[left], a[right] = a[right] ,a[left]
            left += 1
            right -= 1
        return " " .join(a) 

