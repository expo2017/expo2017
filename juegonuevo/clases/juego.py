from .nivel import nivel

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
        nivelaux=nivel()
        nivelaux.setid(n.id)
        nivelaux.settiempo(n.tiempo)
        nivelaux.setjugadas(n.jugadas)
        nivelaux.setfoto(n.foto)
        self.nivelactual=nivelaux

    def reiniciarjuego(self):
        self.puntos=0
        self.start=False
        self.gano=True
        self.listadedirecciones=None
        self.listadedirecciones=[]
        #self.nivelactual=self.niveles[0]



