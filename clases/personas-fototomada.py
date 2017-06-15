class persona (object):
    foto=None
    def __init__(self):
        self.foto=None

    def guardarimagen(self,ruta,imagen):
        self.foto=imagen.save(ruta)

