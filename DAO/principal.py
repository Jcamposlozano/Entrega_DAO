from fabricas import *


f = FabricaJson()
print("*************************************************")
f.readFabricas().readComputador(computador="PC 1"
                            , marca = "AMD"
                            , partes="PROCESADOR")
print("*************************************************")

f.readFabricas().readObject(computador="PC 1"
                            , marca = "AMD"
                            , partes="PROCESADOR")


