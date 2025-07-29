class Solution:
    def solution_1668_4(self, P: List[int], T: List[int]) -> int:
		#Sort
        P, T = sorted(P, reverse=True), sorted(T, reverse=True)
        
		#Original amount of players
        n = len(P)
        
		#Greedy
        while T and P:
            if P[-1] <= T[-1]: P.pop()
            T.pop()
                
		#Amount of players popped
        return n - len(P)