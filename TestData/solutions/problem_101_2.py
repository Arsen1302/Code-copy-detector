class Solution1:
    def solution_101_2(self, s: str) -> str:
        """We create two new arrays to represent the original string. We use
        `groupby` to count the number of repeats of each consecutive letters
        and record them in two arrays. One is letters, recording all
        consecutively distinct letters. The other is indices, recording the
        index of the last appearance of the corresponding letter in letters.

        Let idx = len(indices) - 2. We want to examine whether a palindrome can
        be formed from the start of s with the repeats of letters[idx] being in
        the middle. There are three scenarios.

        1. idx reaches the first letter and still no palindrome insight. We
        need to reverse the substring starting from indices[idx + 1] to the end
        and add it to the front of s.
        
        2. A palindrome is found when idx is not pointing to the first letter
        of s. This means we just need to reverse the remaining of s outside the
        palindrome and add it to the front of s.

        3. idx has not reached the first letter of s, yet a palindrome almost
        forms. By almost forms, it means that the palindrome check has reaches
        the first letter and the first letter is equal to the last letter in
        the current palindrome check, yet the number of repeats of these two
        do not match. In particular, the number of repeats of the first letter
        is smaller than that of the last letter in check. In this case, we can
        simply add to the front the difference in count between the first and
        the last letter to form the palindrome, and then add the reversed
        remaining substring to the front.

        O(N), 56 ms, 73% ranking.
        """
        letters = ['#']
        indices = [-1]
        for k, g in groupby(s):
            letters.append(k)
            indices.append(indices[-1] + len(list(g)))
        idx = len(indices) - 2
        while idx >= 0:
            # scenario 1
            if idx == 1:
                return s[:indices[1]:-1] + s
            # palindrome check
            lo, hi = idx - 1, idx + 1
            while lo >= 1 and hi < len(indices):
                if letters[lo] != letters[hi] or (indices[lo] - indices[lo - 1]) != (indices[hi] - indices[hi - 1]):
                    break
                lo -= 1
                hi += 1
            # scenario 2
            if lo == 0:
                return s[:indices[hi - 1]:-1] + s
            # scenario 3
            if lo == 1 and hi < len(indices) and letters[lo] == letters[hi]:
                dif = (indices[hi] - indices[hi - 1]) - (indices[lo] - indices[lo - 1])
                if dif > 0:
                    return s[:indices[hi]:-1] + letters[lo] * dif + s
            idx -= 1
        return s