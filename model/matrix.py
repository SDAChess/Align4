class Matrix:
    def __init__(self, width, height=None, default_value=None):
        self._width = width
        self._height = height if height else width
        self._matrix = []
        self._init_matrix(default_value)

    def _init_matrix(self, default_value):
        for _ in range(self._height):
            self._matrix.append([])
            for _ in range(self._width):
                self._matrix[-1].append(default_value)

    def __getitem__(self, item):
        x, y = item
        return self._matrix[y][x]

    def __setitem__(self, item, value):
        x, y = item
        self._matrix[y][x] = value
