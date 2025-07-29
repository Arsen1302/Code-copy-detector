class Solution:
    def solution_521_3(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        match = sorted([(idx, i, len(sources[i])) for i, idx in enumerate(indices) if s[idx:].startswith(sources[i])])
        if not match: return s
        ans, cur = '', 0
        for idx, i, n in match:
            ans += s[cur:idx] + targets[i]
            cur = idx + n
        else:
            ans += s[cur:]
        return ans