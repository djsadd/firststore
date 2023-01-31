class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def get(cls):
        return cls.x


point = Point(1, 4)
print(point.get())