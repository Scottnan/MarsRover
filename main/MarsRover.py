import math


class MarsRover:
    def __init__(self, x, y, theta):
        self._x = x
        self._y = y
        self._theta = theta

    def get_location(self):
        return self._x, self._y

    def orient_is_legal(self):
        if 0 <= self._theta < 360:
            return True
        return False

    def get_orientation(self):
        if self._theta >= 360:
            while True:
                self._theta -= 360
                if self.orient_is_legal():
                    return self._theta
        elif self._theta < 0:
            while True:
                self._theta += 360
                if self.orient_is_legal():
                    return self._theta
        return self._theta

    def turnDirection(self, turn):
        if turn == "l":
            self._theta += 90
        elif turn == "r":
            self._theta -= 90

        # 抛出错误
    def Run(self, distance):
        pi = self._theta/180 * math.pi
        self._x = self._x + distance * math.cos(pi)
        self._y = self._y + distance * math.sin(pi)