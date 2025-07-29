class Solution:
    def solution_1371_5(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort(reverse = True)
        unpaired = Counter(); original = []
        for i, num in enumerate(changed):
            if num != 0:
                if unpaired[2 * num] > 0:
                    unpaired[2 * num] -= 1
                    original.append(num)
                elif num % 2 == 0:
                    unpaired[num] += 1
                else:
                    return []
            else:
                unpaired[num] += 1
        
        if unpaired[0] % 2 == 0:
            original += [0] * (unpaired[0] // 2)
            unpaired[0] = 0
        
        return original if all(count == 0 for count in unpaired.values()) else []