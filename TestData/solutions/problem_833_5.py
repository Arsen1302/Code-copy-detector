class Solution:
    def solution_833_5(self, moves: List[List[int]]) -> str:
        game = [['','',''],['','',''],['','','']]
        a = 0
        for i,j in moves:
            if a%2 == 0:
                game[i][j] = 'A'
                a+=1
            else:
                game[i][j] = 'B'
                a+=1
        
        if game[0][0] == game[0][1] == game[0][2] and game[0][0]!='':
            return game[0][0]
        elif game[1][0] == game[1][1] == game[1][2] and game[1][0]!='':
            return game[1][0]
        elif game[2][0] == game[2][1] == game[2][2] and game[2][0]!='':
            return game[2][0]
        elif game[0][0] == game[1][0] == game[2][0] and game[0][0]!='':
            return game[0][0]
        elif game[0][1] == game[1][1] == game[2][1] and game[0][1]!='':
            return game[0][1]
        elif game[0][2] == game[1][2] == game[2][2] and game[0][2]!='':
            return game[0][2]
        elif game[0][0] == game[1][1] == game[2][2] and game[0][0]!='':
            return game[0][0]
        elif game[0][2] == game[1][1] == game[2][0] and game[0][2]!='':
            return game[0][2]
        else:
            for i in game:
                if '' in i:
                    return "Pending"
            return "Draw"