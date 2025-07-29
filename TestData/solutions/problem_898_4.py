class Solution:
    def solution_898_4(self, arr: List[int]) -> List[int]:
        ans = {}
        for i in arr:
            count_1 = bin(i)[2:].count('1')
            if(count_1 in ans):
                ans[count_1].append(i)
            else:
                ans[count_1] = [i]
        
        ans = list(sorted(ans.items() , key=lambda x: x[0]))
        arr = []
        for i , j in ans:
            j.sort()
            arr.extend(j)
        
        return arr