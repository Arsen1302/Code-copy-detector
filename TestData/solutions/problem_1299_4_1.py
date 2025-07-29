class Solution:
    def solution_1299_4_1(self, loginTime: str, logoutTime: str) -> int:
        login = self.solution_1299_4_2(loginTime)
        logout = self.solution_1299_4_2(logoutTime)
        
        if logout < login:  # new day after midnight
            logout = logout + 24 * 60
            
        if logout - login < 15:
            return 0
        
        login = self.solution_1299_4_3(login)
        logout = self.solution_1299_4_4(logout)
        
        return (logout - login) // 15
    
    
    def solution_1299_4_2(self, current_time: str) -> int:
        h, m = map(int, current_time.split(":"))
        return h * 60 + m
    
    def solution_1299_4_3(self, m: int):
        return m if m % 15 == 0 else m + (15 - m % 15)
    
    def solution_1299_4_4(self, m: int):
        return m if m % 15 == 0 else m - (m % 15)