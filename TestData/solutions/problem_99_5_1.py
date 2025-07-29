class Solution:
    def solution_99_5_1(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        rtn = []
        memo = {}
        for word in words:
            self.solution_99_5_2(board, word, memo)
            if not (-1,-1) in memo[word]:
                rtn.append(word)

        validatedRtn = []
        for w in rtn:
            for k in memo[w]:
                if self.solution_99_5_3(board, k[0], k[1], w):
                    validatedRtn.append(w)
                    break
        return validatedRtn

    def solution_99_5_2(self, board, word,  memo):
        if word in memo:
            return

        leftOver = word[1:]
        if leftOver != '':
            self.solution_99_5_2(board, leftOver, memo)
            if (-1, -1) in memo[leftOver]:
                memo[word] = {(-1,-1): 1}
                return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if leftOver == '' or (i,j+1) in memo[leftOver] or (i,j-1) in memo[leftOver] or (i+1,j) in memo[leftOver] or (i-1,j) in memo[leftOver]:
                        if word in memo:
                            memo[word][(i,j)] = 1
                        else:
                            memo[word] = {(i,j): 1}
                    

        if not word in memo:
            memo[word] = {(-1,-1): 1}

    def solution_99_5_3(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.solution_99_5_3(board, i+1, j, word[1:]) or self.solution_99_5_3(board, i-1, j, word[1:]) \
        or self.solution_99_5_3(board, i, j+1, word[1:]) or self.solution_99_5_3(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res