class Solution:  # The plan is to iterate through the words and, for each word w, move 
                     # letter by letter of w though the string s if possible to determine 
                     # whether w is a subsequence of s. If so, we  add to ans.
                     #
                     # We use a function and a cache because many of the words share letter
                     # sequences.

    def solution_482_2_1(self, s: str, words: list[str]) -> int:
                                    
        @lru_cache(None)            
        def solution_482_2_2(word):
            start = 0 

            for ch in word:         
                start = s.find(ch, start) + 1          # <-- find gives us the index of the
                if not start: return False             #     the next occurence of ch after
                                                       #     the index "start"
            return True
        
        return sum(solution_482_2_2(w) for w in words)        # <-- we count all the words that
                                                       #     returned True.