class Solution:
    def solution_1108_3(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for i, piece in enumerate(pieces):
            for j,num in enumerate(piece):
                try: pieces[i][j] = arr.index(num)
                except: return False
        
        pieces.sort()
        
        return [i for i in range(len(arr))] == [x for piece in pieces for x in piece]
		## or use list(chain(*[piece for piece in pieces]))