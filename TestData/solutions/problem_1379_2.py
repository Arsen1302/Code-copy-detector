class Solution:
    def solution_1379_2(self, board: List[List[str]], word: str) -> bool:
        for x in board, zip(*board): 
            for row in x:
                for k, grp in groupby(row, key=lambda x: x != "#"): 
                    grp = list(grp)
                    if k and len(grp) == len(word): 
                        for w in word, word[::-1]: 
                            if all(gg in (" ", ww) for gg, ww in zip(grp, w)): return True 
        return False