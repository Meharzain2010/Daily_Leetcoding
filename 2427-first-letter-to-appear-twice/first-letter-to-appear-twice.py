class Solution:
    def repeatedCharacter(self, s: str) -> str:    
                             #"abccbaacz"
        result = []
        for char in s:      #b
            if char in result:
                return char
            else:
                result.append(char)
            

