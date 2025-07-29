class Solution:
    def solution_989_5(self, arr: List[int], k: int) -> List[int]:
        list.sort(arr)
        m = len(arr) // 2 if len(arr) % 2 == 1 else len(arr) // 2 - 1
        mv = arr[m]
        
        l = 0
        r = 0
        cnt = 0
        ans = []
        while cnt < k:
            if abs(arr[-1-r] - mv) >= abs(arr[l] - mv):
                ans.append(arr[-1-r])
                r += 1
            else:
                ans.append(arr[l])
                l += 1
            cnt += 1
        
        return ans