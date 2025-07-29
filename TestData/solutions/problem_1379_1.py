class Solution:
    def solution_1379_1(self, board: List[List[str]], word: str) -> bool:
        for x in board, zip(*board): 
            for row in x: 
                for s in "".join(row).split("#"): 
                    for w in word, word[::-1]: 
                        if len(s) == len(w) and all(ss in (" ", ww) for ss, ww in zip(s, w)): return True 
        return False