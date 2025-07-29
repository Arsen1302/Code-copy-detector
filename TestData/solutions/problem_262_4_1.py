class Solution:
    def solution_262_4_1(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        remainder = [i+1 for i in range(maxChoosableInteger)] # numbers
        @cache
        def solution_262_4_2(total, remainder):
            if total >= desiredTotal:
                return False # total is already exceed the desiredTotal. Opponent won. 
            
            for num in remainder:
                if solution_262_4_2(total + num, tuple([n for n in remainder if n != num])) == False: # if opponent lose, I win(return True)
                    return True
            return False 
        
        if desiredTotal == 0: 
            return True 
        if sum(remainder) < desiredTotal: # Both of two cannot win.
            return False 
        return solution_262_4_2(0, tuple(remainder))