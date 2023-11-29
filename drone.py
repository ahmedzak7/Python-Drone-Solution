# drone.py

class Drone:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'M':
                self.move_forward()
            elif instruction == 'U':
                self.move_up()
            elif instruction == 'D':
                self.move_down()

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'W':
            self.x -= 1

    def move_up(self):
        self.z += 1

    def move_down(self):
        self.z -= 1

    def __str__(self):
        return f"{self.x} {self.y} {self.z} {self.direction}"
