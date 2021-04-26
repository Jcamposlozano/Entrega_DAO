from abc import ABC, abstractmethod
from dataAccessObject import *

class FabricaAbstracta(ABC):
    @abstractmethod
    def readProcesador(self, **kwargs):
        pass

class FabricaJson(FabricaAbstracta):

    def readProcesador(self, **kwargs):
        return DataAccessObjectJson()

class FabricaXml(FabricaAbstracta):

    def readProcesador(self, **kwargs):
        return DataAccessObjectXml()
