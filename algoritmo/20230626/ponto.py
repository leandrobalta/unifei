class ponto: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def imprimir(self):
        print ("(", self.x, ",", self.y, ")")
        
    def __eq__(self, __value: object) -> bool:
        if self.x == __value.x and self.y == __value.y:
            return True
        else:
            return False
        
    def __ne__(self, __value: object) -> bool:
        if self.x != __value.x or self.y != __value.y:
            return True
        else:
            return False
        
    def __lt__(self, __value: object) -> bool:
        if self.x < __value.x and self.y < __value.y:
            return True
        else:
            return False
        
    def __gt__(self, __value: object) -> bool:
        if self.x > __value.x and self.y > __value.y:
            return True
        else:
            return False