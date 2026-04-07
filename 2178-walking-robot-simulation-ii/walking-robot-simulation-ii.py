class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height) - 4
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        p = self.pos
        if p < self.w:
            return [p, 0]
        p -= (self.w - 1)
        if p < self.h:
            return [self.w - 1, p]
        p -= (self.h - 1)
        if p < self.w:
            return [self.w - 1 - p, self.h - 1]
        p -= (self.w - 1)
        return [0, self.h - 1 - p]

    def getDir(self) -> str:
        p = self.pos
        if p == 0:
            return "South" if self.moved else "East"
        if 0 < p < self.w:
            return "East"
        if self.w <= p < self.w + self.h - 1:
            return "North"
        if self.w + self.h - 1 <= p < 2 * self.w + self.h - 2:
            return "West"
        return "South"