class Solution:
    def solution_585_4(self, s: str, k: int) -> str:
        visited = set()
        if k == 1:
            arr = list(s)

            while "".join(arr) not in visited:
                visited.add("".join(arr))
                ele = arr.pop(0)
                arr.append(ele)
                
            

            return min(visited)

        ans = sorted(s)
        return "".join(ans)