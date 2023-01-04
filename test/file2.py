from file1 import Pais
class Viaje:
    costo = float
    tiempo = float
    valor = float
    pais = Pais("","","","")
    
    def __init__(self,costo,tiempo,valor,pais):
        self.costo = costo
        self.tiempo = tiempo
        self.valor = valor
        self.pais = pais
        
    
print(Viaje.pais)
    
    