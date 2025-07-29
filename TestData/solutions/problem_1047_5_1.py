class Solution:
    def solution_1047_5_1(self, position: List[int], m: int) -> int:
        position = sorted(position)
        def solution_1047_5_2(x):
            prev = float('-inf')
            counter = 0
            for p in position:
                if abs(p-prev) >= x:
                    counter += 1
                    prev = p
            if counter >= m:
                return True
            else:
                return False
        
        l, r = 1, max(position)+1
        while l < r:
            mid = (l+r) // 2
            if not solution_1047_5_2(mid):
                r = mid
            else:
                l = mid+1
        return l-1