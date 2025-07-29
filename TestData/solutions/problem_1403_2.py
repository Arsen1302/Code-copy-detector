class Solution:
    def solution_1403_2(self, arr: List[str], k: int) -> str:
        n = len(arr)
        cnt = defaultdict(int)
        for c in arr:
            cnt[c] += 1
        
        distinct = []
        for i in range(n):
            if cnt[arr[i]] == 1:
                distinct.append(arr[i])
                
        if len(distinct) < k:
            return ""
        else:
            return distinct[k-1]