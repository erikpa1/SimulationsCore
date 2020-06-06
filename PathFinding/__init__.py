from PathFinding.PathFinder import *


if __name__ == '__main__':

    path = Path()
    path.add_path(PathElement(0, 0))
    path.add_path(PathElement(0, 1))
    path.add_path(PathElement(1, 0))
    path.add_path(PathElement(1, 1))
    path.add_path(PathElement(2, 1))
    path.add_path(PathElement(1, 2))
    path.add_path(PathElement(2, 2))
    path.add_path(PathElement(3, 2))
    path.add_path(PathElement(3, 3))

    path.print_in_matrix()
    path.find_path_on_index(0, 6)



