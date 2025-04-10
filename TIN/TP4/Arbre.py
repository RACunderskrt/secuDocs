class Arbre:
    def __init__(self,val, proba):
        self.value = val
        if(proba):
            self.proba = proba
        else:
            self.proba = 0.0000001
        self.left = None
        self.right = None
    
    def __str__(self):
        return "value : " + str(self.value) + " |   probability : " + str(self.proba)
    
    def set_right(self,r):
        self.right = r
    
    def set_left(self,l):
        self.left = l
    
    def add_leaves(self,val1, val2):
        if(val1.proba <= val2.proba):
            self.left =  val1
            self.right = val2
        else:
            self.left =  val2
            self.right = val1
        
        self.proba = val1.proba + val2.proba
