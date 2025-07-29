class Solution:
    def solution_910_4(self, s: str) -> int:
        # define a dict for number of left shifts for each vowel
        vowel2shift = {'a': 4, 'e': 3, 'i': 2, 'o': 1, 'u': 0}
        # define a dict for the index of first appearance of a specific parity
        parity2firstIdx = {0: -1}
        # parity initialized to 00000, each vowel appear 0 time which is even
        ret = parity = 0
        # iterate through each letter of s
        for i, letter in enumerate(s):
            # if letter is a vowel, swap/toggle its corresponding bit
            if letter in vowel2shift:
                parity ^= 1 << vowel2shift[letter]
            # if we've seen this particular parity before, it means each vowel 
            # appeared an even number of time between now and then
            # odd + even = odd
            # even + even = even
            if parity in parity2firstIdx:
                ret = max(ret, i-parity2firstIdx[parity])
            # otherwise, record its index of first appearance
            else:
                parity2firstIdx[parity] = i
        return ret