from main.MarsRover import MarsRover
from main.basic import mars_area, BasicInfo
import unittest


class TestMarsRover(unittest.TestCase):
    def test_init(self):
        info_obj = BasicInfo(2, 2, 'W')
        command = "-l -l -f 10"
        mars_obj = MarsRover(info_obj, command)
        self.assertEqual((2, 2), mars_obj._get_location(), )
        self.assertEqual(270, mars_obj._get_orientation())

    def test_turn_direction(self):
        info_obj = BasicInfo(2, 2, 'N')
        command = "-l -l -f 10"
        mars_obj = MarsRover(info_obj, command)
        mars_obj._turn_direction("l")
        self.assertEqual(mars_obj._get_orientation(), 90)
        mars_obj._turn_direction("r")
        self.assertEqual(mars_obj._get_orientation(), 0)
        mars_obj._turn_direction("r")
        self.assertEqual(mars_obj._get_orientation(), 270)
        mars_obj._turn_direction("r")
        self.assertEqual(mars_obj._get_orientation(), 180)
        mars_obj._turn_direction("l")
        self.assertEqual(mars_obj._get_orientation(), 270)

    def test_run(self):
        info_obj = BasicInfo(2, 2, 'N')
        command = "-l -l -f 10"
        mars_obj = MarsRover(info_obj, command)
        mars_obj.run(mars_area, 4)
        self.assertEqual(mars_obj._get_location(), (2, 6))
        mars_obj.run(mars_area, -7)
        self.assertEqual(mars_obj._get_location(), (2, 9))
        info_obj = BasicInfo(2, 2, 'N')
        command = "-l -l -f 10"
        mars_obj = MarsRover(info_obj, command)
        mars_obj.run(mars_area, 8)
        self.assertEqual(mars_obj._get_location(), (2, 7))


class TestMarsArea(unittest.TestCase):
    def test_is_obstacle(self):
        self.assertEqual(False, mars_area.is_obstacle(1, 2))
        self.assertEqual(False, mars_area.is_obstacle(7, 6))
        self.assertEqual(True, mars_area.is_obstacle(10, 10))
