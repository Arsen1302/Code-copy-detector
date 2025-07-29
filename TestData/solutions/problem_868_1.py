class Solution:
    def solution_868_1(self, n: int) -> List[int]:
        left = 0
        right = n
        ans = []
        while True:
            if str(left).count("0")==0 and str(right).count("0")==0:
                ans.append(left)
                ans.append(right)
                break
            left+=1
            right-=1
        return ans