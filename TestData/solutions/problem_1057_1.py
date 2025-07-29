class Solution:
    def solution_1057_1(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)-m+1):
            count = 1
            x = arr[i:i+m]
            res = 1
            for j in range(i+m,len(arr)-m+1,m):
                if x == arr[j:j+m]:
                    count += 1
                else:
                    res = max(res,count)
                    count = 1
                    x = arr[j:j+m]
            res = max(res,count)
            if res >= k:
                return True
        return False