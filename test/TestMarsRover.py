from main.MarsRover import MarsRover
from main.MarArea import MarsArea
import unittest


class TestMarsRover(unittest.TestCase):
    def test_init(self):
        area = MarsArea(X=100, Y=100)
        mars_obj = MarsRover(x=30, y=20, theta=0)
        self.assertEqual(mars_obj.get_location(), (30, 20))
        self.assertEqual(mars_obj.get_orientation(), 0)
        self.assertEqual(area.get_explore_area(), (100, 100))

    # 判断方向是否合法： 0 - 360
    def test_legal_orientation(self):
        mars_obj = MarsRover(x=30, y=20, theta=720)
        self.assertEqual(mars_obj.orient_is_legal(), False)
        self.assertEqual(mars_obj.get_orientation(), 0)

    # 探索：改变方向
    def test_turn_direction(self):
        mars_obj = MarsRover(x=30, y=20, theta=0)
        mars_obj.turnDirection("l")
        self.assertEqual(mars_obj.get_orientation(), 90)
        mars_obj.turnDirection("r")
        self.assertEqual(mars_obj.get_orientation(), 0)
        mars_obj.turnDirection("r")
        self.assertEqual(mars_obj.get_orientation(), 270)
        mars_obj = MarsRover(x=30, y=20, theta=270)
        mars_obj.turnDirection("l")
        self.assertEqual(mars_obj.get_orientation(), 0)

    # 探索： 行动
    def test_run(self):
        mars_obj = MarsRover(x=30, y=20, theta=0)
        mars_obj.Run(30)
        self.assertEqual(mars_obj.get_location(), (60.0, 20.0))
