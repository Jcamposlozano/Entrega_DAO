from abc import ABC, abstractmethod
from dataAccessObject import *

class FabricaAbstracta(ABC):
    @abstractmethod
    def readFabricas(self, **kwargs):
        pass

class FabricaJson(FabricaAbstracta):

    def readFabricas(self, **kwargs):
        return DataAccessObjectJson()

class FabricaXml(FabricaAbstracta):

    def readFabricas(self, **kwargs):
        return DataAccessObjectXml()

