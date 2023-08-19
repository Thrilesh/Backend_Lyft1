import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.tire import Tire
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCapuletEngine(unittest.TestCase):

    def setUp(self):
        # Create a CapuletEngine instance for testing
        self.engine = CapuletEngine(current_mileage=50000, last_service_mileage=40000)

    def test_needs_service_true(self):
        # Test when the engine needs service
        self.assertTrue(self.engine.needs_service())

    def test_needs_service_false(self):
        # Test when the engine doesn't need service
        self.engine.current_mileage = 41000
        self.assertFalse(self.engine.needs_service())

if __name__ == '__main__':
    unittest.main()


class TestSternmanEngine(unittest.TestCase):

    def setUp(self):
        # Create a SternmanEngine instance for testing
        self.engine_with_warning = SternmanEngine(warning_light_is_on=True)
        self.engine_without_warning = SternmanEngine(warning_light_is_on=False)

    def test_needs_service_with_warning(self):
        # Test when the engine needs service (warning light is on)
        self.assertTrue(self.engine_with_warning.needs_service())

    def test_needs_service_without_warning(self):
        # Test when the engine doesn't need service (warning light is off)
        self.assertFalse(self.engine_without_warning.needs_service())

if __name__ == '__main__':
    unittest.main()
    
class TestWilloughbyEngine(unittest.TestCase):
    def setUp(self):
        # Create a WilloughbyEngine  instance for testing
            self.engine = WilloughbyEngine(current_mileage=100000, last_service_mileage=40000)

    def test_needs_service_true(self):
        # Test when the engine needs service
        self.assertTrue(self.engine.needs_service())

    def test_needs_service_false(self):
        # Test when the engine doesn't need service
        self.engine.current_mileage = 41000
        self.assertFalse(self.engine.needs_service())

if __name__ == '__main__':
    unittest.main()
    
    
class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        # Create a NubbinBattery instance for testing
        self.battery = NubbinBattery(current_date="2023-08-01", last_service_date="2020-08-01")

    def test_needs_service_true(self):
        # Test when the battery needs service
        self.assertTrue(self.battery.needs_service())

    def test_needs_service_false(self):
        # Test when the battery doesn't need service
        self.battery.current_date = "2021-08-01"
        self.assertFalse(self.battery.needs_service())

if __name__ == '__main__':
    unittest.main()


class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        # Create a SpindlerBattery instance for testing
        self.battery = SpindlerBattery(current_date="2024-08-01", last_service_date="2021-08-01")

    def test_needs_service_true(self):
        # Test when the battery needs service
        self.assertTrue(self.battery.needs_service())

    def test_needs_service_false(self):
        # Test when the battery doesn't need service
        self.battery.current_date = "2022-08-01"
        self.assertFalse(self.battery.needs_service())

if __name__ == '__main__':
    unittest.main()
    
    




class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.7, 0.9, 0.6]
        carrigan_tire = CarriganTire(tire_wear)
        self.assertTrue(carrigan_tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.8, 0.7, 0.6, 0.5]
        carrigan_tire = CarriganTire(tire_wear)
        self.assertFalse(carrigan_tire.needs_service())

if __name__ == '__main__':
    unittest.main()
    
    
class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.7, 0.9, 0.6]
        octoprime_tire = OctoprimeTire(tire_wear)
        self.assertTrue(octoprime_tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.8, 0.7, 0.6, 0.5]
        octoprime_tire = OctoprimeTire(tire_wear)
        self.assertFalse(octoprime_tire.needs_service())

if __name__ == '__main__':
    unittest.main()

    