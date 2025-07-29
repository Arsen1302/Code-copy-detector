class Solution:
    def solution_561_5_1(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        # Initialize 
        self.obsticles_dict = {f"{x},{y}": 1 for [x,y] in obstacles}
        self.cur_position = {'x':0, 'y':0}
        self.cur_direction = 0
        self.max_distance = 0
        
        # Run through each command
        for command in commands:
            if command < 0: self.solution_561_5_2(command)
            else: self.solution_561_5_3(command)
            self.solution_561_5_4()
        return self.max_distance
        
    def solution_561_5_2(self, command: int) -> None:
        rotation = +1 if command == -1 else -1 
        self.cur_direction = (self.cur_direction + rotation) % 4

    def solution_561_5_3(self, command: int) -> None:
        cur_position = self.cur_position.copy()
        for step in range(command):
            if self.cur_direction == 0:   cur_position['y'] += 1 # North
            elif self.cur_direction == 1: cur_position['x'] += 1 # East
            elif self.cur_direction == 2: cur_position['y'] -= 1 # South
            elif self.cur_direction == 3: cur_position['x'] -= 1 # West

            if f"{cur_position['x']},{cur_position['y']}" in self.obsticles_dict:
                return None
            else:
                self.cur_position = cur_position.copy()
        
    def solution_561_5_4(self) -> None: 
        self.max_distance = max(
            self.cur_position['x']**2 + self.cur_position['y']**2,
            self.max_distance
        )