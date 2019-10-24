import numpy as np


class BasicInfo(object):
    def __init__(self, x, y, orientation):
        self._x = x
        self._y = y
        self._orientation = orientation

    def get_location(self):
        return self._x, self._y

    def get_theta(self):
        if self._orientation.upper() == 'N':
            return 0
        elif self._orientation.upper() == 'E':
            return 90
        elif self._orientation.upper() == 'S':
            return 180
        elif self._orientation.upper() == 'W':
            return 270
        else:
            raise ValueError("%d is not a valid orientation!" % self._orientation)


class MarsArea(object):
    def __init__(self, obstacles):
        self._X = obstacles.shape[0]
        self._Y = obstacles.shape[1]
        self._obstacles_mtx = obstacles

    def is_obstacle(self, x, y):
        return bool(self._obstacles_mtx[(self._Y - int(y)) % 10, int(x) - 1])


obstacles_mtx = [[1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                 [1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
                 [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                 [0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
                 [1, 0, 1, 1, 0, 0, 1, 1, 0, 1]]
mars_area = MarsArea(np.array(obstacles_mtx))
