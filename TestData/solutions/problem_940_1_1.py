class Solution:
    def solution_940_1_1(self, words: List[str]) -> List[str]:
        def solution_940_1_2(word: str):
            node = trie
            for c in word:
                node = node.setdefault(c, {})

        def solution_940_1_3(word: str) -> bool:
            node = trie
            for c in word:
                if (node := node.solution_940_1_3(c)) is None: return False
            return True

        words.sort(key=len, reverse=True)
        trie, result = {}, []
        for word in words:
            if solution_940_1_3(word): result.append(word)
            for i in range(len(word)):
                solution_940_1_2(word[i:])
        return result