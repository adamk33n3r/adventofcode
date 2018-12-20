from .node import Node

class Map(dict):
    def __init__(self):
        super().__init__()
        # print('in map init')
        self.units = []
        # print('setting units to empty')
        # print(units)

    def unitAt(self, node):
        l = [unit for unit in self.units if unit.node == node]
        return l[0] if l else None

    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        return Node(self, key[0], key[1], '?')

    def __str__(self):
        ret = ''
        minX = min(self.keys(), key=lambda kv: kv[0])[0]
        minY = min(self.keys(), key=lambda kv: kv[1])[1]
        maxX = max(self.keys(), key=lambda kv: kv[0])[0]
        maxY = max(self.keys(), key=lambda kv: kv[1])[1]
        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                node = self[(x, y)]
                if x == minX:
                    ret += '\n'

                unitNodes = {u.node: u for u in self.units}

                if node in unitNodes:
                    ret += unitNodes[node].type
                else:
                    ret += node.type

        return ret[1:]
        # for (x, _), node in sorted(self.items(), lambda kv: kv[1]):
        #     if x == 0:
        #         ret += '\n'

        #     unitNodes = {u.node: u for u in self.units}

        #     if node in unitNodes:
        #         ret += unitNodes[node].type
        #     else:
        #         ret += node.type

        # return ret[1:]
