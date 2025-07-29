class Solution:
    def solution_266_1_1(self, words: List[str]) -> List[str]:
        ddic = lambda: defaultdict(ddic)
        trie = ddic()
        
        for word in words:
            cur = trie
            for char in word:
                cur = cur[char]

            cur['end'] = True
        
        def solution_266_1_2(word, start):
            cur = trie
            for i in range(start, len(word)):
                char = word[i]
                if char not in cur:
                    return False
                cur = cur[char]

                if 'end' in cur:
                    if i + 1 == len(word):
                        # tricky part that helps us distinguish simple word from concat word
                        return start != 0
                    
                    if solution_266_1_2(word, i + 1):
                        return True

            return False
            
        return [word for word in words if solution_266_1_2(word, 0)]