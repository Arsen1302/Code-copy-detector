class Solution:
    def solution_1684_5(self, num1: int, num2: int) -> int:
        # determine number of 1's in binary representation
        # which is also equal to bin(num2[1:]).count("1")
        n2 = 0
        while num2:
            if num2 &amp; 1:    # last bit is 1
                n2 += 1     # increase count
            num2 >>= 1      # shift the binary number to the right

        # search for indices for 0's and 1's
        # n = 110 (binary form) => bits1{0: [0], 1: [1, 2]}
        bits1 = {0: [], 1: []}
        i = 0    # index from the right side
        while num1:
            if num1 &amp; 1:   # decide which list to append
                bits1[1].append(i)
            else:
                bits1[0].append(i)
            i += 1        # increase index
            num1 >>= 1    # shift the number to the right

        # list of positions - reversed for 1 (left to right)
        # straight for 0 (right to left)
        target_pos = bits1[1][::-1] + bits1[0]    # positions for 1
        # if we need more 1's to be placed into the target number
        if len(target_pos) < n2:
            next_pos = target_pos[0] + 1    # most left position
            # fill it in with consecutive positions
            target_pos += list(range(next_pos,
                                     next_pos + n2 - len(target_pos)))
        # cut the list to the required length n2
        target_pos = target_pos[:n2]
        # find the final number by shifting 1's to the target positions
        # e.g. target = 101 == 100 + 001 in binary
        return sum(1 << pos for pos in target_pos)