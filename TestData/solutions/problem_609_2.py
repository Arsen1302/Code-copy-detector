class Solution:
    def solution_609_2(self, arr: List[int]) -> List[int]:
        # gather the indices of the ones
        ones = [i for i, d in enumerate(arr) if d == 1]

        if not ones:
            return [0, 2]
        elif len(ones) % 3 != 0:
            return [-1, -1]

        # get the start indices of the 3 groups
        i, j, k = ones[0], ones[len(ones)//3], ones[len(ones)//3*2]

        # calculate the size/length of what each group should be
        length = len(arr) - k  # note that the last/rightmost group must include all digits till the end
                               # so we know that the size of each group is `len(arr) - k` (where `k` is start of third group)

        # compare the three groups
        if arr[i:i+length] == arr[j:j+length] == arr[k:k+length]:
            return [i+length-1, j+length]
        
        return [-1, -1]