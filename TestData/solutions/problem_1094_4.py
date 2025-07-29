class Solution:
    def solution_1094_4(self, arr: List[int]) -> float:
        arr.sort() #Sorting list
        per = ceil(0.05 * len(arr)) #calculating 5% of length of list
        while per!=0: #removing 5% of first and last elements from the list
            arr.pop()
            arr.pop(0)
            per-=1
        
        return sum(arr)/len(arr)  #returning mean