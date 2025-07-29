class Solution:
    def solution_1586_2(self, password):
        return re.match(r'^(?!.*(.)\1)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&amp;*()+-]).{8,}$', password)