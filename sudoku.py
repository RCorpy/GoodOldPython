mesa=[
        [6,0,7,2,0,3,0,9,1],
        [9,0,0,6,5,0,0,0,0],
        [8,0,2,0,0,9,0,0,0],
        [0,9,0,5,7,0,0,0,6],
        [0,8,0,0,1,0,0,7,0],
        [2,0,0,0,3,8,0,4,0],
        [0,0,0,7,0,0,6,0,3],
        [0,0,0,0,2,5,0,0,8],
        [5,3,0,8,0,4,7,0,9]]

class Sudoku():
    def __init__(self, mesa):
        self.mesa = mesa
        self.resolver()

    def validar(self, num, pos):

        for i in range(len(self.mesa[0])):
            if self.mesa[pos[0]][i]==num and pos[1]!=i:
                return False
        for j in range(len(self.mesa)):
            if self.mesa[j][pos[1]] == num and pos[0]!=j:
                return False
        x = pos[0]//3
        y = pos[1]//3

        for k in range(0,3):
            for l in range(0,3):
                if num == self.mesa[3*x+k][3*y+l] and pos[0] != 3*x+k and pos[1] != 3*y+l:
                    return False
        return True

    def resolver(self):
        
        encontrado = self.encontrar_vacio()
        if not encontrado:
            return True
        else:
            fila= encontrado[0]
            colum = encontrado[1]

        for i in range(1,10):
            if self.validar(i , (fila, colum)):
                self.mesa[fila][colum]= i
                if self.resolver():
                    return True

                self.mesa[fila][colum]= 0 
        return False       

    def encontrar_vacio(self):
        for i in range(len(self.mesa)):
            for j in range(len(self.mesa)):
                if self.mesa[i][j] == 0:
                    return (i,j) #colum, fila
        return None

    def imprimir(self):
        for idx, i in enumerate(self.mesa):
            if idx%3 == 0 and idx !=0:
                print("-------------------")
            for idx2,j in enumerate(i):
                print(str(j)+" ", end="")
                if idx2 == 8:
                    print("")
                elif idx2%3 ==2:
                    print("|", end= "")


Sudoku(mesa).imprimir()