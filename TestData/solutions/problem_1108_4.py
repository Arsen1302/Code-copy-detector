class Solution:
    def solution_1108_4(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {}
        for piece in pieces:
            dic[piece[0]] = piece
        idx = 0
        while idx < len(arr):
            key = arr[idx]
            if key in dic:
                if arr[idx: idx + len(dic[key])] == dic[key]:
                    idx += len(dic[key])
                else:
                    return False
            else:
                return False
        return True