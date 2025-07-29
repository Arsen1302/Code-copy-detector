class Solution:
                    # Criteria for a valid transormation:

                    #   1) The # of Ls, # of Rs , and # of _s must be equal between the two strings
                    #
                    #   2) The ordering of Ls and Rs in the two strings must be the same.
                    #
                    #   3) Ls can only move left and Rs can only move right, so each L in start 
                    #      cannot be to the left of its corresponding L in target, and each R cannot
                    #      be to the right of its corresponding R in target.

    def solution_1615_1(self, start: str, target: str) -> bool:
                                                          
        if (len(start) != len(target) or 
            start.count('_') != target.count('_')): return False   #  <-- Criterion 1

        s = [(ch,i) for i, ch in enumerate(start ) if ch != '_']
        t = [(ch,i) for i, ch in enumerate(target) if ch != '_']

        for i in range(len(s)):
            (sc, si), (tc,ti) = s[i], t[i]
            if sc != tc: return False                              # <-- Criteria 1 &amp; 2
            if sc == 'L' and si < ti: return False                 # <-- Criterion 3
            if sc == 'R' and si > ti: return False                 # <--/

        return True                                                # <-- It's a winner!