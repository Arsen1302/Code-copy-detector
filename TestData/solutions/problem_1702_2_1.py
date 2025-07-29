class Solution:
    def solution_1702_2_1(self, words: List[str]) -> str:
        
        # go through all of the words find and track all the diffs
        cn = collections.defaultdict(list)
        for idx, word in enumerate(words):
            
            # get the difference array
            diff_arr = Solution.solution_1702_2_2(word)

            # append to the counter
            cn[diff_arr].append(idx)
        
        # get the searched element
        ele = min(cn.values(), key=len)
        return words[ele[0]]
    
    @staticmethod
    def solution_1702_2_2(word: str):
        return tuple(map(lambda x: ord(word[x[0]]) - ord(x[1]), zip(range(1,len(word)), word[:-1])))