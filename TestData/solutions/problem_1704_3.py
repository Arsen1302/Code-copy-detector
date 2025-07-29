class Solution:
    def solution_1704_3(self, nums: List[int], space: int) -> int:

        # get a dict of modulos
        modulo_dict = dict()

        # go through the array and compute the modulo and their counter
        for idx, num in enumerate(nums):
            # compute the modulo
            modi = num % space

            # check whether we need to create one
            if modi in modulo_dict:

                # keep track of the smalles number
                modulo_dict[modi][0] = min(num, modulo_dict[modi][0])

                # keep track of the count of this specific modulo
                modulo_dict[modi][1] += 1
            else:

                # create this modulo
                modulo_dict[modi] = [num, 1]
        
        # go through the dict and element with the highest modulo count
        best_ele = max(modulo_dict.values(), key=lambda x: (x[1], -x[0]))
        
        # return the good element
        return best_ele[0]