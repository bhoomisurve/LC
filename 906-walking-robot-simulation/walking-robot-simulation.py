class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacle_set = set(map(tuple, obstacles))
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacle_set:
                        x += dx[di]
                        y += dy[di]
                        max_dist_sq = max(max_dist_sq, x*x + y*y)
                    else:
                        break
                        
        return max_dist_sq