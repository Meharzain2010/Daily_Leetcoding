class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Input: ops = ["5","2","C","D","+"]
        Output: 30
        """
        stack = []
        for op in operations:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
                
        return sum(stack)
         