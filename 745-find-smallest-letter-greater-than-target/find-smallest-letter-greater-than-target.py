class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
                            # ("a","d","q","q","z")   [d]
        for i in letters:   
            if i > target:
                return i
        return letters[0]