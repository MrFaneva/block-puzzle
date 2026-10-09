class Score:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lines = 0

    def add_lines(self, n):
        self.lines += n
        self.score += (n * 100) * self.level
        self.level = self.lines // 10 + 1
