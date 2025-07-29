class Solution:
    def solution_1674_5(self, words: List[str]) -> List[int]:
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                if ch in node:
                    node = node[ch]
                    node["$"] += 1
                else:
                    node[ch] = {"$": 1}
                    node = node[ch]

        result = []
        for w in words:
            node = trie
            total = 0
            for ch in w:
                total += node[ch]["$"]
                node = node[ch]
            result.append(total)
        return result