class Solution:
    def solution_99_3_1(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        Trie = lambda : defaultdict(Trie)
        root = Trie()
        def solution_99_3_2(s):
            cur = root
            for c in s: cur = cur[c]
            cur['$'] = s
                
        for word in words: solution_99_3_2(word)
        m, n = len(board), len(board[0])
        
        def solution_99_3_3(i, j, root):
            ch = board[i][j]
            cur = root.get(ch)
            if not cur: return 

            if '$' in cur: 
                res.append(cur['$'])
                del cur['$']
            
            board[i][j] = '#'
            if i<m-1: solution_99_3_3(i+1, j, cur)
            if i>0: solution_99_3_3(i-1, j, cur)
            if j<n-1: solution_99_3_3(i, j+1, cur)
            if j>0: solution_99_3_3(i, j-1, cur)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                solution_99_3_3(i, j, root)
        return res