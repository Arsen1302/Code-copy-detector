class Solution:
    def solution_854_1(self, board: List[str]) -> List[int]:
        """bottom-up dp"""
        n = len(board) #dimension

        #count > 0 also indicates state is reachable
        dp = [[0, 0] for _ in range(n+1)] #score-count (augment by 1 for convenience)
        
        for i in reversed(range(n)):
            #not assuming reachability while updating state
            copy = [[0, 0] for _ in range(n+1)] #to be updated to new dp
            for j in reversed(range(n)): 
                if board[i][j] == "X": continue #skip obstacle
                if board[i][j] == "S": #initialize "S"
                    copy[j] = [0, 1]
                    continue 
                #find max score from neighbors
                for candidate in (copy[j+1], dp[j], dp[j+1]): #right/below/right-below
                    if not candidate[1]: continue #not reachable
                    if copy[j][0] < candidate[0]: copy[j] = candidate[:]
                    elif copy[j][0] == candidate[0]: copy[j][1] = (copy[j][1] + candidate[1])%(10**9+7)
                #update with board number 
                if board[i][j] != "E": copy[j][0] += int(board[i][j])
            dp = copy
        return dp[0]