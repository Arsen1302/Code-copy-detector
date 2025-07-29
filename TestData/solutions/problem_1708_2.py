class Solution:
    def solution_1708_2(self, n: int, target: int) -> int:

        # the sum of digits by addition only gets smaller if we
        # get zeros certain digits by going to the next power
        # of ten for that digit, which increases the previous
        # digit by one
        
        # lets get the digits of the number
        digits = [int(ch) for ch in list(str(n))]
        
        # compute the prefix sum for the digits
        digits_acc = list(itertools.accumulate(digits))

        # check the last sum to immediately break
        if digits_acc[-1] <= target:
            return 0
        
        # go through the digits and check when we are lower than
        # the target
        found = False
        for idx in range(len(digits)-1, -1, -1):
            if digits_acc[idx] < target:
                found = True
                break
        
        # now get the number
        if found:
            number = reduce(lambda x, y: x*10 + y, digits[:idx+1]) + 1
            number *= 10**(len(digits)-idx-1)
        else:
            number = 10**(len(digits))

        return number - n