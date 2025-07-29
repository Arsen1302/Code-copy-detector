class Solution:
    def solution_1442_3(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        alice,bob = 0,len(plants)-1
        result,capacity_A,capacity_B = 0,capacityA,capacityB
        while alice < bob:
            if capacity_A < plants[alice]:
                capacity_A = capacityA
                result += 1
            capacity_A -= plants[alice]
            if capacity_B < plants[bob]:
                capacity_B = capacityB
                result += 1
            capacity_B -= plants[bob]
            alice += 1
            bob -= 1
        if alice == bob:
            max_capacity = max(capacity_A,capacity_B)
            if max_capacity < plants[alice]: result += 1
        return result