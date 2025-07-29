class Solution:
    def solution_942_2_1(self, text: str) -> str:
        def solution_942_2_2(entity: str, symbol: str):
            node = trie
            for c in entity:
                node = node.setdefault(c, {})
            node['#'] = symbol

        def solution_942_2_3(idx: int) -> tuple:
            node = trie
            while text[idx] in node:
                node = node[text[idx]]
                idx += 1
                if '#' in node: return node['#'], idx
            return False, idx

        def solution_942_2_4():
            i = 0
            while i < len(text):
                if text[i] in trie:
                    symbol, j = solution_942_2_3(i)
                    yield symbol or text[i:j]
                    i = j
                else:
                    yield text[i]
                    i += 1

        trie = {}
        entities = [('&amp;quot;', '"'), ('&amp;apos;', "'"), ('&amp;amp;', '&amp;'), ('&amp;gt;', '>'), ('&amp;lt;', '<'), ('&amp;frasl;', '/')]
        for entity, symbol in entities:
            solution_942_2_2(entity, symbol)
        return ''.join(solution_942_2_4())