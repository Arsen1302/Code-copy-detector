class Solution(object):
    def solution_560_2(self, arr):
        n = len(arr)
        
        longest = defaultdict(int)
        index = {}
        for i in range(n):
            index[arr[i]] = i 
          
        res = 0 
        for i in range(n):
            for j in range(i+1, n):
                k = arr[i] + arr[j]
                if k in index:
                    idx = index[k]
                    longest[(j, idx)] = longest[(i, j)] + 1
                    res = max(res, longest[(j, idx)])
        if res >= 1:
            return res+2
        else:
            return 0