import random


class Tile:
    def __init__(self):
        self.visited = False
        self.sides = {}


class Maze:
    def __init__(self, s):
        self.side = s
        self.array = []

    def new_array(self):
        for y in range(self.side):
            self.array.append([])
            for x in range(self.side):
                self.array[y].append(Tile())

        for y in range(self.side):
            for x in range(self.side):
                tile = self.array[y][x]
                if x > 0:
                    tile.sides[self.array[y][x - 1]] = [False, 'east']
                if x < self.side - 1:
                    tile.sides[self.array[y][x + 1]] = [False, 'west']
                if y > 0:
                    tile.sides[self.array[y - 1][x]] = [False, 'north']
                if y < self.side - 1:
                    tile.sides[self.array[y + 1][x]] = [False, 'south']

    def generate(self):
        current = self.array[0][0]
        queue = [current]
        while True:
            not_visited_neighbors = []
            current.visited = True
            for s in current.sides:
                if not s.visited:
                    not_visited_neighbors.append(s)

            if not not_visited_neighbors:
                queue.remove(current)
                if queue:
                    current = queue[-1]
                else:
                    break

            else:
                chosen = random.choice(not_visited_neighbors)
                queue.append(chosen)
                chosen.sides[current][0] = True
                current.sides[chosen][0] = True
                current = chosen

    def print_maze(self):
        for y in range(len(self.array)):
            for x in self.array[y]:
                sides = {x.sides[s][1]: x.sides[s][0] for s in x.sides}
                symbol = '   '
                if 'north' in sides and sides['north']:
                    symbol = ' # '

                print(symbol, end='')

            print('')

            for x in self.array[y]:
                sides = {x.sides[s][1]: x.sides[s][0] for s in x.sides}
                symbol1 = ' '
                symbol2 = ' '

                if 'east' in sides and sides['east']:
                    symbol1 = '#'

                if 'west' in sides and sides['west']:
                    symbol2 = '#'

                print(symbol1, end='')
                print('0', end='')
                print(symbol2, end='')

            print('')

            for x in self.array[y]:
                sides = {x.sides[s][1]: x.sides[s][0] for s in x.sides}
                symbol = '   '
                if 'south' in sides and sides['south']:
                    symbol = ' # '

                print(symbol, end='')

            print('')


if __name__ == "__main__":
    side = 10
    maze = Maze(side)
    maze.new_array()
    maze.generate()
    maze.print_maze()
    print('end')