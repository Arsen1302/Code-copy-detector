class Solution:
    def solution_1045_5(self, arr):
        return 3 in accumulate(arr,lambda x,y:x+y%2 if y%2 else 0, initial=0)