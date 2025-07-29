class Solution:
    def solution_980_3(self, target: List[int], arr: List[int]) -> bool:
        if len(target)!=len(arr):
            return False
        for i in target:
            if i not in arr:
                return False
        target.sort()
        arr.sort()
        for i in range(len(arr)):
            if arr[i]!= target[i]:
                return False
        return True