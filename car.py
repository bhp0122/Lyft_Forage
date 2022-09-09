from abc import ABC, abstractmethod


# Factory Method
class Serviceable(object):
    def needs_service(self):
        pass


class Car(ABC):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()


# Composition: Engine & Battery cannot exist without Car????
'''
Engines:
1. Capulet
2. Willoughby
3. Sternman
'''


class Engine(ABC):
    def need(self):
        pass


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = int(last_service_mileage)
        self.current_mileage = int(current_mileage)

    def needs_service(self):
        if (self.current_mileage - self.last_service_mileage) > 30000:
            return True
        else:
            return False
        # BETTER/REMEMBER/REDUCTION: return (self.current_mileage - self.last_service_mileage) > 30000


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = int(last_service_mileage)
        self.current_mileage = int(current_mileage)

    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) > 60000

    # BETTER/REMEMBER/REDUCTION: return (self.current_mileage - self.last_service_mileage) > 60000


class SternmanEngine(Engine):
    def __init__(self, warning_light):
        self.warning_light = warning_light

    def needs_service(self):
        if self.warning_light:
            return True
        else:
            return False


'''
Batteries:
1. Spindler
2. Nubbins
'''


class Battery(ABC):
    def needs_service(self):
        pass


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        # Do not format date????
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.current_date.year - self.last_service_date.year >= 3:
            return True
        else:
            return False


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # Add years to last_service_date & then compare to current_date
        if self.current_date.year - self.last_service_date.year >= 4:
            return True
        else:
            return False


'''
Tire Servicing
'''


class Tire(ABC):
    def needs_service(self):
        pass


class CarriganTires(Tire):
    def __init__(self, _array):
        self._array = _array

    def needs_service(self):
        for values in self._array:
            if values >= 0.9:
                return True


class OctoPrimeTires(Tire):
    def __init__(self, _array):
        self._array = _array

    def needs_service(self):
        total = 0
        for values in self._array:
            total += values
            if total >= 3.0:
                return True
        # REDUCE: sum(self._array) >= 3.0

'''
Car Factory
'''

'''
Static method cannot access class attributes or instance attributes. 

It can return an object of the class

"A method defined as a member of an object but is accessible directly 
from an API object's constructor, rather than from an object instance 
created via the constructor."

'''


class CarFactory(Car):
    @staticmethod
    def create_calliope(self, last_service_date, current_date, last_service_mileage, current_mileage, _array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTires(_array)

        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(self, last_service_date, current_date, last_service_mileage, current_mileage, _array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTires(_array)

        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(self, last_service_date, current_date, warning_light, _array):
        engine = SternmanEngine(warning_light)
        battery = SpindlerBattery(last_service_date, current_date)

        tire = OctoPrimeTires(_array)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(self, last_service_date, current_date, last_service_mileage, current_mileage, _array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)

        tire = CarriganTires(_array)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(self, last_service_date, current_date, last_service_mileage, current_mileage, _array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)

        tire = OctoPrimeTires(_array)
        car = Car(engine, battery, tire)
        return car
