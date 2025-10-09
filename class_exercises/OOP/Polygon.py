import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, hypot


class Coord:
    def __init__(self, x1: float, y1: float):
        self.point = np.array((x1, y1))

    def distance(self, other) -> float:
        pass


class Polygon:
    def __init__(self, points: list[Coord]):
        self.points = points

    def perimeter(self) -> float:
        pass

    def plot(self):
        pass


class Triangle(Polygon):
    def __init__(self, p0: Coord, p1: Coord, p2: Coord):
        pass

    def area(self) -> float:
        pass
