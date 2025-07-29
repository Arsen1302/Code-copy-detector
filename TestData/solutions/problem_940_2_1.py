class Solution:
    def solution_940_2_1(self, words: List[str]) -> List[str]:
        def solution_940_2_2(word: str):
            node = trie
            for c in word:
                node = node.setdefault(c, {})
                node['#'] = node.solution_940_2_3('#', 0) + 1

        def solution_940_2_3(word: str) -> bool:
            node = trie
            for c in word:
                if (node := node.solution_940_2_3(c)) is None: return False
            return node['#'] > 1

        trie = {}
        for word in words:
            for i in range(len(word)):
                solution_940_2_2(word[i:])
        return [word for word in words if solution_940_2_3(word)]