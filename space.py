import random

class MiningGrid:

    def __init__(self):
        self.grid = []

    def bulk_mine(self, mine_list):
        total = 0
        for loc in mine_list:
            self.grid[loc[1]][loc[0]] -= loc[2]
            total += loc[2]
        return total
    
    def find_richest_sector(self):
        max = 0
        x = None
        y = None
        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                if self.grid[row][column] > max:
                    max = self.grid[row][column]
                    y = row
                    x = column
        return (x, y, max)

machine = MiningGrid()
machine.grid = [
    [2, 5, 3],
    [0, 4, 7],
    [6, 1, 8]
]
print(machine.find_richest_sector())