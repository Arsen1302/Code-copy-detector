class Solution:
    cur_dir = 'N'
    def solution_720_3_1(self, instructions: str) -> bool:
        self.cur_dir = 'N'
        cur_pos = [0,0]
        for ins in instructions:
            if ins == 'G':
                self.solution_720_3_2(cur_pos)
            else:
                self.solution_720_3_3(ins)
        if cur_pos[0] == 0 and cur_pos[1] == 0:
            return True
        if self.cur_dir != 'N':
            return True
        return False
        
    def solution_720_3_2(self,cur_pos):
        if self.cur_dir == 'N':
            cur_pos[1] += 1
        elif self.cur_dir == 'S':
            cur_pos[1] -= 1
        elif self.cur_dir == 'W':
            cur_pos[0] -= 1
        elif self.cur_dir == 'E':
            cur_pos[0] += 1
            
    #think of a compass...and all possiblities of change in direction
    def solution_720_3_3(self,d):
        if self.cur_dir == 'N' and d == 'L':
            self.cur_dir = 'W'
        elif self.cur_dir == 'N' and d == 'R':
            self.cur_dir = 'E'
        elif self.cur_dir == 'S' and d == 'L':
            self.cur_dir = 'E'
        elif self.cur_dir == 'S' and d == 'R':
            self.cur_dir = 'W'
        elif self.cur_dir == 'W' and d == 'L':
            self.cur_dir = 'S'
        elif self.cur_dir == 'W' and d == 'R':
            self.cur_dir = 'N'
        elif self.cur_dir == 'E' and d == 'L':
            self.cur_dir = 'N'
        elif self.cur_dir == 'E' and d == 'R':
            self.cur_dir = 'S'