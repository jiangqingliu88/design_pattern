from abc import ABCMeta, abstractmethod

class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass

class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

# 高层的代码不应该依赖那些它不需要的接口
class Tiger(LandAnimal):
    def walk(self):
        pass

# 高层的代码不应该依赖那些它不需要的接口
class Frog(LandAnimal, WaterAnimal):
    def walk(self):
        pass