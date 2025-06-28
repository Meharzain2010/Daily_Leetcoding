class Solution:
    def isPalindrome(self, x: int) -> bool:

        # -------------------------Easy------------------------

        # x = str(x)
        # X = x[:: -1]
        # if x == X:
        #     return True
        # else:
        #     return False

        # -------------------------Medium------------------------
        # x = str(x)
        # X = x[:: -1]
        # if x == X:

         # -------------------------Hard------------------------

        return str(x) == str(x)[::-1]
