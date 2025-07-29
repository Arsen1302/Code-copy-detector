class Solution:
    def solution_1473_3_1(self, differences: List[int], lower: int, upper: int) -> int:
        l = lower
        r = upper
        right = float("-inf")

        while l <= r:
            mid = l+r>>1

            isHidden,condition = self.solution_1473_3_2(differences,mid,lower,upper)
            if isHidden:
                right = mid
                l = mid + 1
            else:
                if condition == "HIGH": r = mid - 1
                else: l = mid + 1
        
        l = lower
        r = upper
        left = float("inf")

        while l <= r:
            mid = l+r>>1

            isHidden,condition = self.solution_1473_3_2(differences,mid,lower,upper)
            if isHidden:
                left = mid
                r = mid - 1
            else:
                if condition == "HIGH": r = mid - 1
                else: l = mid + 1

        if right == float("-inf") or left == float("inf"): return 0
        return right - left + 1

    def solution_1473_3_2(self,differences,start,lower,upper):
        cur_sum = start
        for difference in differences:
            cur_sum += difference
            if cur_sum < lower: return False,"LOW"
            if cur_sum > upper: return False,"HIGH"

        return True,"PERFECT"