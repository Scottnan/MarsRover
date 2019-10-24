import math
import numpy as np


class MarsRover(object):
    def __init__(self, basic_info, command):
        self._x, self._y = basic_info.get_location()
        self._theta = basic_info.get_theta()
        self._command = command

    def _get_location(self):
        return self._x, self._y

    def _get_orientation(self):
        return self._theta

    def _turn_direction(self, turn):
        if turn == "l":
            self._theta += 90
            self._theta %= 360
        elif turn == "r":
            self._theta += 270
            self._theta %= 360

    def run(self, mars_area, distance):
        if distance == 0:
            return
        else:
            pi = self._theta / 180 * math.pi
            target_x = (self._x + np.sign(distance) * math.sin(pi) + 10) % 10
            target_y = (self._y + np.sign(distance) * math.cos(pi) + 10) % 10
            print(target_x, target_y)
            if self._explore_location(mars_area, (target_x, target_y)) is True:
                return 0
            else:
                self._x, self._y = target_x, target_y
                return self.run(mars_area, distance - np.sign(distance))

    @staticmethod
    def _explore_location(mars_area, loc):
        return mars_area.is_obstacle(*loc)

    def exe_command(self):
        command_iter = iter(self._command.split(" "))
        try:
            i = next(command_iter)
            if i[1] == l:
