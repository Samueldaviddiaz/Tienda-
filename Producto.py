
class Producto:
    def __init__(self, producto, precio, iva, cantidad, caducidad, promocion, factura):
        self.producto = producto
        self.precio = precio
        self.iva = iva
        self.cantidad = cantidad
        self.caducidad = caducidad
        self.promocion = promocion
        self.factura = factura

    def vender(self):
        return self.producto + self.precio + self.iva + self.cantidad + self.caducidad + self.promocion +self.factura

    def comprar(self):
        return self.producto + self.precio + self.iva + self.cantidad + self.caducidad + self.promocion +self.factura