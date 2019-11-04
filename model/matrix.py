class Matrix:
    def __init__(self, size, default_value=None):
        self.size = size
        self.create_matrix(default_value)

    def create_matrix(self, default_value):
        for i in range(self.size):
            self.matrix.append([])
            for j in range(self.size):
                self.matrix[-1].append(default_value)

    def getCell(self, x, y):
        return self[x][y]
