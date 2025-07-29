class Solution:
    def solution_900_4(self, n: int) -> int:
        """
        Considering we know the solution for n = 1: (P1, D1), now we want to find the solution for n = 2:
        the idea is that: 
        we can insert P2 at 3 positions: either before P1, between P1 and D1, or after D1.
        lets look at each case separately:
            - case (P2, P1, D1):
                now we can place D2 in 3 possible positions: after P2, or after P1 or after D1.
            - case (P1, P2, D1):
                we can only place D2 after P2, or after D1.
            - case (P1, D1, P2)
                the only place for D2 is right after P2.
        The total possible solution for n = 2 is therefore 3+2+1 = 6
        
        Same logic now to find n = 3.
        the solutions for n = 2 are: (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1), (P2,D2,P1,D1)
        For each of those solutions, we may place P3 at 5 different places: at position 1, or 2, or 3, or 4 or at the end.
        if we placed P3 at position 1, then D3 can be placed either at position 2, 3, 4, 5 or at the end. Giving us 5 possibilities.
        now if P3 is at position 2, then D3 can only by at 3, 4, 5, or at the end. 4 possibilities.
        and so on.
        Basically, for each of the n = 2 solution, we have 5+4+3+2+1 = 15 solutions.
        So the number total solutions for n = 3 is size(solution n = 2) * 15, which is here 6 * 15 = 90.
        
        Now we can use a DP table (or just a variable to optimize space) to track the number of solutions for n-1.
        we also need the length of each solution for layer n-1. That can be found easily (for a layer i, the length of solution is n 2*i)
        and we have (2i+1) + (2i) + (2i-1) + ... + (1) solutions. Which is an arithmetic sequence. That sum is (2i+1)*(2i+1 + 1)/2
        
        Below is the implementation in Python3:
        """
        
        dp = [1]*n
        modulo = 1e9 +7
        for i in range(1, n):
            x = 2*i + 1
            dp[i] = dp[i-1] * (x*(x+1)//2) % modulo
        return int(dp[-1])