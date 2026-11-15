class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        Did the robot return to the origin? → It's bounded (will repeat forever)
        Is the robot NOT facing north anymore? → It's bounded (will eventually return after a few cycles)
        '''
        x = y = 0
        dx, dy = 0, 1 # facing north
        for c in instructions:
            if c == "G": x += dx; y += dy
            elif c == "L": dx, dy = -dy, dx
            else: dx, dy = dy, -dx
        return (x == 0 and y == 0) or (dx, dy) != (0, 1)
