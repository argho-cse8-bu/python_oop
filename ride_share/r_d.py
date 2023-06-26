# from _typeshed import SupportsWrite
from abc import ABC, ABCMeta,abstractmethod
from datetime import datetime
class Ride_sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.riders = []

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)
    
    def __repr__(self) -> str:
        return (f'{self.company_name} with riders: {len(self.riders)} and driver: {len(self.drivers)}')

class user: 
    def __init__(self,name,email,nid) -> None:
        self.name = name
        self.email = email
        # TODO: set user id dynamycally
        self.__id = 0
        self.__NID = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(user):
    def __init__(self, name, email, nid, current_location, initial_ammount) -> None:
        self.current_ride = None
        self.wallet = initial_ammount
        self.current_location = current_location
        
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider with name: {self.name} and email {self.email}')
    
    def load_cash(self, amount):
        if amount>0:
            self.wallet+=amount

    def Update_location(self, current_location):
        self.current_location=current_location

    def request_ride(self,destination,  location = None):
        if not self.current_ride:
            # Todo : set ride peoperty
            # TODO: set current ride via ride match
            ride_request = Ride_request(self, destination)
            ride_matcher = Ride_matching
            self.current_ride =ride_matcher.find_driver(ride_request)

    def show_current_ride(self):
        print(self.current_ride)

class driver(user):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f'Driver with name: {self.name} and email: {self.email}')

    
    def accep_ride(self, ride):
        ride.set_driver(self)

class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_location = None
        self.end_location = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def  start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f'Ride details. Started: {self.start_location} to {self.end_location}'


class Ride_request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class Ride_matching:
    def __init__(self) -> None:
        self.drivers = []
    
    def find_driver(self, ride_request):
        if len(self.availavle_drivers) > 0:
            # TODO: find the closest driver of the driver
            driver = self.availavle_drivers[0]
            ride = Rider(Ride_request.rider.current_location, Ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        
class Vehicle(ABC):
    speed = {
        'car': 50,
        'Bike': 60,
        'cng': 30
    }

    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = "available"
        super().__init__()

    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'unavailable'


#checj the class intigration
nie_jaw = Ride_sharing('Nie Jaw')
sakib = Rider('Sakib Khan', 'Sakib@khan.com', 1234, 'mohakhali', 1200)
nie_jaw.add_rider(sakib)
roton_toto = driver('roton_toto', 'roton@toto.com', 1333, 'gulshan 1')
nie_jaw.add_driver(roton_toto)
print(nie_jaw)
sakib.request_ride('uttora')
print(sakib.show_current_ride())
