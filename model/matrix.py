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

    def __len__(self):
        return self._width, self._height

    def __str__(self):
        string = "|"
        for y in range(self.height - 1, -1, -1):
            string += ' '.join(map(lambda player: str(player), self._matrix[y])) + '|\n|'
        string = string[:-1]
        return string

    def __repr__(self):
        return str(self)

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width
