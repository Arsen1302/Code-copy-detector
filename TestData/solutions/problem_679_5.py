class Solution:
    def solution_679_5(self, board: List[List[str]]) -> int:
        res=0
        n_row=len(board)
        n_col=len(board[0])
        dirs=[[0,1],[0,-1],[-1,0],[1,0]]
        for i in range(n_row):
            for j in range(n_col):
                if board[i][j]=="R":
                    for dir in dirs:
                        cur_r=i
                        cur_c=j
                        while 0<=cur_r<n_row and 0<=cur_c<n_col:
                            if board[cur_r][cur_c]=='B':
                                break
                            if board[cur_r][cur_c]=="p":
                                res+=1
                                break
                            cur_r+=dir[0]
                            cur_c+=dir[1]
                    return res
        return 0