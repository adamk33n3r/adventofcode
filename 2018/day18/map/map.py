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

    def __str__(self):
        ret = ''
        for (x, _), node in self.items():
            if x == 0:
                ret += '\n'

            unitNodes = {u.node: u for u in self.units}

            if node in unitNodes:
                ret += unitNodes[node].type
            else:
                ret += node.type

        return ret[1:]
