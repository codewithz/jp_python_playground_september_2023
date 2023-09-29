# abc -- abstract base class
# abc.ABC -- Abstact Base Class
# abc.@abstractmethod -- which makes a function abstract

from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

# --------------------------------------------

class HondaCity(Car):
    def brakes(self):
        print("Brakes")

    def start(self):
        print("Start of Honda City")

    def stop(self):
        print("Stop of Honda City")

 #----------------------------------

h=HondaCity()
h.start()
h.stop()
