class Solution:
    def solution_653_2(self, s: str, t: str) -> bool:
        repeat = 1000
        
        res =  []
                
        for word in (s, t):
            stack = []
            for char in word:
                if char == ")":
                    nums = ""
                    char = ""
                    
                    while char != "(" and stack:
                        nums += char
                        char = stack.pop(-1)
        
                    stack.append( nums[::-1] * repeat )
                else:
                    stack.append(char)
            
            res.append(("".join(stack))[:100])
            
        return float(res[0]) == float(res[1])
                    

        ```