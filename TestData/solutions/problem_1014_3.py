class Solution:
    def solution_1014_3(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        sum_arr=[]
        for i in range(0, n):
            s=0
            for j in range(i, n):
                s+=nums[j]
                sum_arr.append(s)
        sum_arr.sort()
        print(sum_arr)
        return sum(sum_arr[left-1: right])%1000000007