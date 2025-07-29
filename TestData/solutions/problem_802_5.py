class Solution:
    def solution_802_5(self, arr: List[int], difference: int) -> int:
        """
                     7  8   5  3  2  1     dif = -2
        previous     9. 10. 8. 5. 4  3
        key          7  8.  5  3  4  1 
        previoulen   1  1   2  3  1  4
        
        
        key is the ending integer in subsequence,
        value is the length of subsequence ending with key
        
        ma
        """
        mapping = {}
        for i in arr:
            previous = i - difference
            if previous not in mapping.keys():
                mapping[i] = 1
            else:
                mapping[i] = mapping[previous] + 1
        res = max(mapping.values())
        return res