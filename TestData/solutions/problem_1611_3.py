class Solution:
    def solution_1611_3(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        ans = 0
        p = 0
        for departure in buses:
            count = 0
            while count < capacity and p < len(passengers) and passengers[p] <= departure:
                count += 1
                if p == 0 or passengers[p] - 1 > passengers[p - 1]:
                    ans = passengers[p] - 1
                p += 1
            if count < capacity:
                if p == 0 or passengers[p - 1] < departure:
                    ans = departure
        return ans