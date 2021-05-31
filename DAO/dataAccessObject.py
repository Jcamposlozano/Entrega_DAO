import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
from abc import ABC, abstractmethod

class DataAccessObjectJson:

    @abstractmethod
    def readObject(self, **kwargs):
        with open('./data/data.json') as json_file:
            data = json.load(json_file)
            for c in data:
                if c["componentes"]["marca"] == kwargs["marca"]:
                    print(c["componentes"]["partes"][str(kwargs["partes"]).lower()])
                        


    @abstractmethod
    def readComputador(self, **kwargs):
        with open('./data/data.json') as json_file:
            data = json.load(json_file)
            for c in data:
                if c["computador"] == kwargs["computador"]:
                    print("computador", c["computador"])
                    print("**** marca = ",c["componentes"]["marca"],"****")
                    
                    for p, v in c["componentes"]["partes"].items():
                        print(p," = ", v)


class DataAccessObjectXml:

    @abstractmethod
    def readObject(self, **kwargs):
        # parse an xml file by name
        tree = ET.parse('./data/data.xml')
        root = tree.getroot()

        for elem in root:
            if str(elem.attrib["title"]).upper() == kwargs["marca"]:
                for subelem in elem:
                    if str(subelem.tag).lower() == str(kwargs["partes"]).lower():
                        print(subelem.text, "SOURCE: XML")
    @abstractmethod
    def readComputador(self, **kwargs):
        pass
