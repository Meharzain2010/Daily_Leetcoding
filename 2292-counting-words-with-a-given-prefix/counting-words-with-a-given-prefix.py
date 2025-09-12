class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #words = ["pay","attention","practice","attend"], 
        #pref = "at"
        output = []
        for word in words:
            if word.startswith(pref):
                output.append(word)
        return len(output)
            