class juego (object):
    puntos=0
    listadedirecciones=[]
    start=False
    gano=True
    niveles=[]
    nivelactual=None

    def setpuntos(self):
        self.puntos+=1
    def setdireccion(self,d):
        self.listadedirecciones.append(d)
    def setstart(self,s):
        self.start=s
    def setgano(self,g):
        self.gano=g
    def setnivel(self,n):
        self.niveles.append(n)
    def setnivelactual(self,n):
        self.nivelactual=n

    def reiniciarjuego(self):
        self.puntos=0
        self.start=False
        self.gano=True
        self.nivelactual=None


