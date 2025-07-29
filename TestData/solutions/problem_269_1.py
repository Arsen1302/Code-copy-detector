class Solution:
    def solution_269_1(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        if len(heaters) == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))

        m_value = -1
        f, s, ind_heat = heaters[0], heaters[1], 2
        for i in range(len(houses)):
            while houses[i] > s and ind_heat < len(heaters):
                f, s = s, heaters[ind_heat]
                ind_heat += 1
            m_value = max(m_value, min(abs(houses[i] - f), abs(houses[i] - s)))
        return m_value