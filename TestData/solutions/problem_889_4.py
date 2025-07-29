class Solution:
    def solution_889_4(self, arr: List[int], k: int, threshold: int) -> int:
        # start with the sum of first k elements
        summ = sum(arr[:k])
        
        # set out(result) variable to 1
        # if the first set of sum is valid
        # i.e its avg >= threshold
        out = 1 if summ//k >= threshold else 0
        
        # start the loop from 1, since we've
        # already taken into account the elements
        # from i = 0.
        # go till k elements less than the length
        # that is the length of our window and since
        # it has to be inclusive, add 1 to the range
        for i in range(1, len(arr)-k+1):
            # remove the last element from the sum
            # and add the next element (i+k-1)
            summ -= arr[i-1]
            summ += arr[i+k-1]
            
            # increment counter if avg >= threshold
            if summ//k >= threshold: out += 1
            
        return out