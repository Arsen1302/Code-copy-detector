class Solution:
    def solution_1453_5(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        ans = []
        
        for i in range(len(s)):
            
            # create short version of instructions 
            # for current iteration 
            instructions = s[i:]
            
            cnt = 0
            x, y = startPos[0], startPos[1]
            
            # for every instruction in this iteration
            for inst in instructions:
                
                # move
                if inst == "R":
                    y += 1
                elif inst == "L":
                    y -= 1
                elif inst == "D":
                    x += 1
                else:
                    x -= 1
            
                # check conditions
                if x < 0 or y < 0 or x >= n or y >= n:
                    break
                
                # counting steps
                cnt += 1
                
            ans.append(cnt)
        return ans