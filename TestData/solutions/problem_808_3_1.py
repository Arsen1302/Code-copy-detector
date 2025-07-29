class Solution:
    def solution_808_3_1(self, nums: List[int]) -> int:
        longest = 0
        charToFreq = defaultdict(int)
        freqToChars = defaultdict(int)
        for i, c in enumerate(nums):
            freq = charToFreq[c]
            
            if freq in freqToChars:
                freqToChars[freq] -= 1
                if freqToChars[freq] == 0:
                    del freqToChars[freq]
                
            freqToChars[freq+1] += 1
            charToFreq[c] += 1
            if self.solution_808_3_2(freqToChars):
                longest = i+1

        return longest

    # Four valid cases:
    # 1. All numbers have frequency of 1 => {1 : n}
    # 2. There's only a single number k  => {n : 1}
    # 3. All but one numbers have the same frequency and the odd one is an singleton
    #                                    => {1 : 1, someFreq : k}
    # 4. All but one numbers have the same frequency and the odd one has a frequency of exactly 1 higher
    #                                    => {maxFreq : 1, (maxFreq-1) : k}
    def solution_808_3_2(self, freqToChars):
        numKeys = len(freqToChars.keys())
        if numKeys == 1:
            firstKey = list(freqToChars.keys())[0]
            # all have freq of 1 or there's only a single char
            return firstKey == 1 or freqToChars[firstKey] == 1
        if numKeys > 2:
            return False

        entries = sorted(list(freqToChars.items()))
        singleton = entries[0][0] == 1 and entries[0][1] == 1
        freqDiffOne = entries[1][0] - entries[0][0] == 1
        higherSingleton = entries[1][1] == 1
        return singleton or (higherSingleton and freqDiffOne)