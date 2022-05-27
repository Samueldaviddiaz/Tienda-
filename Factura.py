
class Factura:
    def __init__(self, producto, precio, iva, cantidad, promocion, recibe, devuelve, pedido, vendedor, fecha, id):
        self.producto = producto
        self.precio = precio
        self.iva = iva
        self.cantidad = cantidad
        self.promocion = promocion
        self.recibe = recibe
        self.devuelve = devuelve
        self.pedido = pedido
        self.vendedor = vendedor
        self.fecha = fecha
        self.id = id

    def imprimir(self):
        pass
    