import random

class MiningGrid:

    def __init__(self):
        self.grid = []

    def bulk_mine(self, mine_list):
        for loc in mine_list:
            