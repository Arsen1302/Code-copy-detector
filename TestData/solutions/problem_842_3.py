class Solution:
    def solution_842_3(self, new: List[List[int]]) -> int:
        arr=[]
        for i in range(len(new)):
            for j in range(len(new)):
                if i!=j and new[j][0] <= new[i][0] and new[i][1] <= new[j][1]:
                    arr.append(new[i])
                    break
        return len(new)-len(arr)