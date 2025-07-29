class Solution:
    def solution_793_4(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        diffs = defaultdict(list)
        
        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i + 1])
            
            diffs[diff].append([arr[i] , arr[i + 1]])
            
        return(diffs[min(diffs.keys())])