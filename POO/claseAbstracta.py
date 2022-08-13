# ABC Abstract Base Class
from abc import ABC, abstractmethod


# Asi obligamos a que las clases hijas deban implementar el metodo calcular area y esto hace que la clase se vuelva
# abstracta por lo que ya no se podra crear instancias de este metodo
class Ejemplo(ABC):
    @abstractmethod
    def CalcularArea(self):
        pass
