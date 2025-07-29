class Solution:
    def solution_1647_4(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        energy_gain = experience_gain = 0
        for ene in energy:
            if initialEnergy - ene < 1:
                energy_gain += ene + 1 - initialEnergy
                initialEnergy = ene + 1 
            initialEnergy -= ene

        for exp in experience:
            if initialExperience - exp < 1:
                experience_gain += exp + 1 - initialExperience
                initialExperience = exp + 1
            initialExperience += exp
        return energy_gain + experience_gain