class direccion (object):
    iddireccion=None
    fotodireccion=None
    botonarriba=None
    botonabajo=None
    botonizquierda=None
    botonderecha=None
    condicion=None
    nivel=None

    def setid(self,iddirec):
        self.iddireccion=iddirec

    def setfoto(self,direc):
        self.fotodireccion=direc

    def setarriba(self,bin):
        self.botonarriba=bin

    def setabajo(self,bin):
        self.botonabajo=bin

    def setderecha(self,bin):
        self.botonderecha=bin

    def setizquierda(self,bin):
        self.botonizquierda=bin

    def setcondicion (self,con):
        self.condicion=con

    def setnivel(self,nivel):
        self.nivel=nivel

