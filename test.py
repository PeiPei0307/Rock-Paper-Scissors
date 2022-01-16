class Employee:
    def __init__(self):
        self.cut_tree = 3

class Andy(Employee):
    def __init__(self, get_gold):
        super().__init__()
        self.get_gold = get_gold

    def getDetials(self):
        print('==getDetals==')
        print('tree:', self.cut_tree)
        print('gold:', self.get_gold)


if __name__ == "__main__":
    andy = Andy(1)
    andy.getDetials()