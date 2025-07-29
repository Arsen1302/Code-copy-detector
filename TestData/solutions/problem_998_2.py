class Solution:
    def solution_998_2(self, names: List[str]) -> List[str]:
        seen = {}
        for name in names: 
            if name not in seen: seen[name] = 1
            else: 
                k = seen[name]
                while (suffix := f"{name}({k})") in seen: k += 1
                seen[name] = k+1
                seen[suffix] = 1
        return seen.keys()