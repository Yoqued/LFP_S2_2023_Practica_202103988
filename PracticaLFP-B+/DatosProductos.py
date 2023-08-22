class productos:
    def __init__(self, nombre,cantidad,precio,ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.ubicacion = ubicacion
    
    def getNombre(self):
        return self.nombre
    def getCantidad(self):
        return self.cantidad
    def getPrecio(self):
        return self.precio
    def getUbicacion(self):
        return self.ubicacion
    
    def setNombre(self, nombre):
        self.nombre = nombre
    def setCantidad(self, cantidad):
        self.cantidad = cantidad
    def setPrecio(self, precio):
        self.precio = precio
    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion
    
    def __repr__(self):
        return f"{self.nombre},{self.cantidad},{self.precio},{self.ubicacion}"