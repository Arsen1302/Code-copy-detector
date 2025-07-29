class Solution:
    def solution_214_3_1(self, stones: List[int]) -> bool:
        
        # will store valid stone positions
        stoneSet = set(stones)
        
        # will store (stone, jumpsize) which will not lead to the last stone
        stoneReach = set()
        
        # set target
        self.last = stones[-1]
        # stoneReach[self.last] = True
        
        def solution_214_3_2(curStone, lastJump):
            
            #check if target
            if curStone==self.last:
                return True
            
            #check if valid stone
            if curStone not in stoneSet:
                return False
            
            # for all possible jumps
            for jump in (lastJump-1, lastJump, lastJump+1):
                
                nextStone = curStone+jump
                # if jumpsize>0 and if (stone, jumpsize) already encounterd 
                # and does not lead to target
                if jump and (nextStone, jump) not in stoneReach:    
                    if self.last==nextStone:
                        return True
                    else:
                        if solution_214_3_2(nextStone, jump):
                            return True
                        # add (stone, jumpsize) if the function returns False
                        stoneReach.add((nextStone, jump))                
            return False
                        
        # Check if stone at position 1
        if 1 not in stoneSet:
            return False
        
        return solution_214_3_2(1, 1)