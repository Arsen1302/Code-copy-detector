class Solution:
    def solution_1108_5(self, arr: List[int], pieces: List[List[int]]) -> bool:
        s = ''.join(map(str, arr))
        for i in pieces:
            if ''.join(map(str, i)) not in s or not i[0] in arr:
                return False
        return True