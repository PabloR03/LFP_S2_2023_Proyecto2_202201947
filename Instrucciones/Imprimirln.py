from Abstract.Abstract import Expression
promt =  ">>>"
class Imprimirln(Expression):

        def __init__(self, texto, fila, columna):
            self.texto = texto
            super().__init__(fila, columna)

        def operar(self, arbol):
            pass

        def ejecutarT(self):
            return promt + self.texto

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()