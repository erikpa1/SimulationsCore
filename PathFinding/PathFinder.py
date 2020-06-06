import math


def get_distance(x, y, z):
    return math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))

class PathElement():

    def __init__(self, x, y, z=0, w=1, h=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h

    def distance(self):
        return get_distance(self.x, self.y, self.z)

    def get_mid(self):
        return (self.x + self.w / 2, self.y + self.h / 2, self.z)


class Path():

    def __init__(self):
        self._paths = []
        self._edges = []

    def add_path(self, path):

        i_index = 0
        for i in self._paths:
            if (self._are_neighbors(path, i)):
                self._edges.append((i_index, len(self._paths)))
            i_index += 1

        self._paths.append(path)

    def find_path_on_index(self, a_point: int, b_point: int):
        start_point = self._paths[a_point]
        end_point = self._paths[b_point]

    def _are_neighbors(self, a, b):

        dis_x = a.x - b.x
        dis_y = a.y - b.y
        dis_z = a.z - b.z

        dist = get_distance(dis_x, dis_y, dis_z)

        return True if dist == 1 else False



    def _print_paths_distance(self):
        for i in self._paths:
            print(i.distance())

    def _make_visualisation_matrix(self):

        maxX: int = 0
        maxY: int = 0

        for i in self._paths:
            if i.x > maxX:
                maxX = i.x

            if i.y > maxY:
                maxY = i.y

        return [[0 for x in range(maxX + 1)] for y in range(maxY + 1)]

    def print_in_matrix(self):

        matrix = self._make_visualisation_matrix()

        for i in self._paths:
            #print(i.x, ":", i.y)
            matrix[i.y][i.x] = "x"

        for x in matrix:
            for y in x:
                print(y, end="")
            print("")

    def print_neighbors(self):
        for i in self._edges:
            print(i)


