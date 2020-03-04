# Tienes un tablero de ajedrez, pero tan solo de 4 x 4, eres capaz de colocar 4 reinas en el tablero?
# La norma es que no haya ninguna reina que este en posicion de comerse otra reina

class Reinas():

    def __init__(self):
        self.solucion = [-1,-1,-1,-1]
        self.resolver()

    def get_position(self):
        for idx, i in enumerate(self.solucion):
            if i == -1:
                return idx
        return None
    
    def check_position(self, idx, check):
        for idx2,i in enumerate(self.solucion):
            if idx2 != idx and i >=0:
                #horizontal
                if check== i:
                    return False
                #diagonal1
                if check==self.solucion[idx2]+idx-idx2:
                    return False
                #diagonal2
                if check==self.solucion[idx2]-idx+idx2:
                    return False
        print("possibility found: " +str(check)+ " index: "+str(idx))
        return True


    def resolver(self):
        
        idx = self.get_position()
        if idx == None:
            return True
        for i in range(len(self.solucion)):
            
            if self.check_position(idx,i):
                self.solucion[idx]= i
                if self.resolver():
                    return True
                else:
                    self.solucion[idx]= -1
    def imprimir(self):
        for i in range(len(self.solucion)):
            for j in range(len(self.solucion)):
                if self.solucion[j]==i:
                    print("Q  ", end = "")
                else:
                    print (".  ", end = "")
                if j == 3:
                    print("\n")
x = Reinas()
print(x.imprimir())

