import unittest
from datetime import date

from car_draft import SpindlerBattery
from car_draft import NubbinBattery

from car_draft import CapuletEngine
from car_draft import SternmanEngine
from car_draft import WilloughbyEngine

from car_draft import CarriganTires
from car_draft import OctoPrimeTires


class TestSpindlerBatter(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2015-01-25")

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


class TestNubbinBatter(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 2999
        last_service_mileage = 0

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 15000
        last_service_mileage = 0

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())


class TestCarriganTires(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        _array = [0.9, 0.7, 0.6, 0.4]

        tire = CarriganTires(_array)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        _array = [0.8, 0.7, 0.8, 0.4]

        tire = CarriganTires(_array)
        self.assertFalse(tire.needs_service())


class TestOptoPrimeTires(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        _array = [0.9, 0.9, 0.8, 0.7]

        tire = OctoPrimeTires(_array)
        self.assertTrue(_array)

    def test_tire_should_not_be_serviced(self):
        _array = [0.5, 0.5, 0.2, 0.2]

        tire = OctoPrimeTires(_array)
        self.assertTrue(_array)


if __name__ == '__main__':
    unittest.main()
