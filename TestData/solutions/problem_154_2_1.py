class Solution:
    def solution_154_2_1(self, string: str) -> str:
        lastIndex = [0] * 26
        self.solution_154_2_2(string, lastIndex)
        stack = self.solution_154_2_3(string, lastIndex)
        
        return ''.join(chr(ord('a') + char) for char in stack)
               
    def solution_154_2_2(self, string, lastIndex):
        for idx, char in enumerate(string):
            lastIndex[ord(char)-ord('a')] = idx         

    def solution_154_2_3(self, string, lastIndex):
        seen = [False] * 26
        stack = []
        
        for idx, char in enumerate(string):
            currentCharVal = (ord(char) - ord('a'))
            if seen[currentCharVal]:
                continue
                
            while (len(stack) > 0 and 
            stack[len(stack)-1] > currentCharVal and
            idx < lastIndex[stack[len(stack)-1]]):
                seen[stack.pop()] = False
                                                                                  
            stack.append(currentCharVal)
            seen[currentCharVal] = True
            
        return stack