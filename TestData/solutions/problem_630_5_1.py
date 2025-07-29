class Solution:
    def solution_630_5_1(self, arr: List[int]) -> str:
        def solution_630_5_2(num):
            if num[0] > 2 : return False
            if num[0] == 2 and num[1] > 3: return False
            if num[2] > 5 : return False
            return True
        p = itertools.permutations(arr)
        ans = None
        for i in p:
            if solution_630_5_2(i) == True:
                if ans == None or i > ans: ans = i
        if ans == None:return ""
        return str(ans[0])+str(ans[1])+':'+str(ans[2])+str(ans[3])