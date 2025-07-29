class Solution:
    def solution_1084_4(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        We can firstly push the number in smallest rowSum and colSum, and push the remain number.
        Time comlexity: O(n)(sort use O(nlogn)), space comlexity: O(1)(if ignore the space of answer and sort the rowSum and colSum in-place)
        """
        # Generate a matrix contain 0
        ans=[[0]*len(colSum) for _ in range(len(rowSum))]

        # Enumarate rowNum and colNum and sort them by value
        row,col=[[i,rowSum[i]]for i in range(len(rowSum))],[[i,colSum[i]]for i in range(len(colSum))]
        row.sort(key=lambda x:x[1])
        col.sort(key=lambda x:x[1])

        # From smallest rowSum and colSum, push the min(rowSum,colSum) into the position of them, keep it from exceeding the both sum.
        # Pop the smaller one, because it has been total used, and the other one minus the amount. 
        while row and col:
            if row[0][1]<=col[0][1]:
                ans[row[0][0]][col[0][0]]=row[0][1]
                col[0][1]-=row[0][1]
                row.pop(0)
            else:
                ans[row[0][0]][col[0][0]]=col[0][1]
                row[0][1]-=col[0][1]
                col.pop(0)
        return ans