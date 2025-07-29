class Solution:
    def solution_635_1(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        for n in sorted(arr, key=abs):
            if count[n] == 0:
                continue
            if count[n * 2] == 0:
                return False
            count[n] -= 1
            count[n * 2] -= 1
        
        return True