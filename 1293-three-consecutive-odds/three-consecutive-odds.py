class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        step 1: jo number 2 pr divide kr raha ho us k 
        step 2:
        step 3:
        """
        if len(arr) < 3:
            return False 
            
        for i in range(len(arr) - 2):    # [1,2,34,3,4,5,7,23,12]
            if (arr[i] % 2 != 0) and (arr[i+1] % 2 != 0) and (arr[i+2] % 2 != 0):
                return True
        return False
        
                        
                