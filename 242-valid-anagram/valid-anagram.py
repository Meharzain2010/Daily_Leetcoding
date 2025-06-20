# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s = list(s)
#         t = list(t) 
#         a = s.sort()       point to be noted       it should be      s.sort() 
#         b = t.sort()       point to be noted       it shoudl be      t.sort()
#         if s == t:
#             return True
#         else:
#             return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        if a==b:
            return True
        else:
            return False




