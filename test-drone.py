import unittest
#import file drone
from drone import Drone

class TestDrone(unittest.TestCase):
    def test_initialization(self):
        drone = Drone(1, 2, 3, 'N')
        self.assertEqual(drone.x, 1)
        self.assertEqual(drone.y, 2)
        self.assertEqual(drone.z, 3)
        self.assertEqual(drone.direction, 'N')

    def test_turn_left(self):
        drone = Drone(0, 0, 0, 'N')
        drone.turn_left()
        self.assertEqual(drone.direction, 'W')

        drone.turn_left()
        self.assertEqual(drone.direction, 'S')

    def test_turn_right(self):
        drone = Drone(0, 0, 0, 'N')
        drone.turn_right()
        self.assertEqual(drone.direction, 'E')

        drone.turn_right()
        self.assertEqual(drone.direction, 'S')

    def test_move_forward(self):
        drone = Drone(1, 1, 1, 'N')
        drone.move_forward()
        self.assertEqual(drone.y, 2)

        drone.turn_right()
        drone.move_forward()
        self.assertEqual(drone.x, 2)

    def test_move_up(self):
        drone = Drone(0, 0, 0, 'N')
        drone.move_up()
        self.assertEqual(drone.z, 1)

    def test_move_down(self):
        drone = Drone(0, 0, 1, 'N')
        drone.move_down()
        self.assertEqual(drone.z, 0)

if __name__ == '__main__':
    unittest.main()
