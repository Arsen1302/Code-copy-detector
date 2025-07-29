class Solution:
    def solution_1094_2(self, arr: List[int]) -> float:
        arr.sort()
        
        n = len(arr)
        per = int(n*5/100)
        l2 = arr[per:len(arr)-per]
		
        x = sum(l2)/len(l2)

        return x