class Product:

    def __init__(self, name, price, quant):
        self.Name = str(name)
        self.Price = float(price)
        self.Quant = int(quant)


    def setName(self, name):
        self.Name = name

    def setPrice(self, price):
        self.Price = price
    
    def setQuant(self, quant):
        self.Quant = quant

    def getName(self):
        return self.Name
    
    def getPrice(self):
        return self.Price
    
    def getQuant(self):
        return self.Quant

    def presentProduct(self):
        print('Nombre: ', self.Name, ' Precio: ', self.Price, ' Cantidad: ', self.Quant)