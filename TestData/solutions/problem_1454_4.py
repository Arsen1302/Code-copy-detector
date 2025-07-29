class Solution:
    def solution_1454_4(self, arr: List[int]) -> List[int]:
        
        # make a dict to save indices
        idces = collections.defaultdict(list)
        
        # search for all common numbers and make the computations
        for idx, num in enumerate(arr):
            
            # check whether we already found one
            idces[num].append(idx)
            
        # reset the array
        arr = [0 for _ in arr]
        
        # go through all of the numbers and calculate the sums
        for ls in idces.values():
            
            # go through all other elements
            for idx, num in enumerate(ls):
                for idx2, num2 in enumerate(ls):
                    if idx != idx2:
                        arr[num] += abs(num-num2)
        return arr