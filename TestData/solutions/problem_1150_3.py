class Solution:
    def solution_1150_3(self, customers: List[List[int]]) -> float:
        ans = 0
        c = -1
        for i in range(0,len(customers)):
            if c>customers[i][0]:
                c = c+customers[i][1]
                ans+=(c)-customers[i][0]
                
            else:
                ans+=customers[i][1]
                c = customers[i][1]+customers[i][0]
                
        return ans/len(customers)