class Solution:
    def solution_1674_4_1(self, words: List[str]) -> List[int]:
        trie = {}
        
        def solution_1674_4_2(trie, word):
            for i in range(len(word)):
                letter = word[i]
                if letter in trie:
                    trie[letter]['count'] += 1
                else:
                    trie[letter] = {}
                    trie[letter]['count'] = 1
                trie = trie[letter]

        for word in words: solution_1674_4_2(trie, word)
        
        def solution_1674_4_3(trie, word):
            count = 0
            for i in range(len(word)):
                letter = word[i]
                count += trie[letter]['count']
                trie = trie[letter]
            return count

        output = []        
        for word in words:
            output.append(solution_1674_4_3(trie, word))
        return output