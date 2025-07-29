class Solution:
    def solution_262_3_1(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 1,2,3,4,5 -> player 1
        # 2,3,4,5 -> player 2, choose any of them, cannot win
        # Then 1 win
        candidate = [i for i in range(1, maxChoosableInteger + 1)]

        if sum(candidate) < desiredTotal:
            return False
        
        memo = dict()
        def solution_262_3_2(candidate, remain):
            if candidate[-1] >= remain:
                return True
            
            if tuple(candidate) in memo:
                return memo[tuple(candidate)]
            
            for i in range(len(candidate)):
                if not solution_262_3_2(candidate[:i] + candidate[i + 1:], remain - candidate[i]):
                    memo[tuple(candidate)] = True
                    return True
            
            memo[tuple(candidate)] = False
            return False
                
        return solution_262_3_2(candidate, desiredTotal)