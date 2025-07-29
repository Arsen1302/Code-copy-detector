class Solution:
def solution_1379_3(self, board: List[List[str]], word: str) -> bool:
    
    words = [word,word[::-1]]
    n = len(word)
    for B in board,zip(*board):
        for row in B:
            q = ''.join(row).split("#")
			for w in words:
                for s in q:
                    if len(s)==n:
                        for i in range(n):
                            if all(s[i]==" " or s[i]==w[i] for i in range(n)):          # If you didn't get here then go beloe for detailed one.
                                return True
            
    return False