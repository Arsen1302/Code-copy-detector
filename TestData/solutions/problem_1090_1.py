class Solution:
    def solution_1090_1(self, s: str) -> int:
        depths = [0]
        
        count = 0
        for i in s:
            if(i == '('):
                count += 1
            elif(i == ')'):
                count -= 1
            depths.append(count)
        
        return max(depths)