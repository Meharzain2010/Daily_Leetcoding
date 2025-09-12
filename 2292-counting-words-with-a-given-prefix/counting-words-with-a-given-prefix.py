class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #words = ["pay","attention","practice","attend"], 
        #pref = "at"
        output = []
        for word in words:
            if word.startswith(pref):
                output.append(word)
        return len(output)
        
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #words = ["pay","attention","practice","attend"], 
        #pref = "at"
        output = 0
        for word in words:
            if word.startswith(pref):
                output  += 1
        return output

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #words = ["pay","attention","practice","attend"], 
        #pref = "at"
        count = 0
        pref_length = len(pref)
        for word in words:
            if word[:pref_length] == pref:
                count +=1
        return count
