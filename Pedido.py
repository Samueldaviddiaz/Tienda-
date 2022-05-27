
class Pedido:
    def __init__(self, vendedor, cliente, proveedor, inventario, producto, factura, productos):
        self.vendedor = vendedor
        self.cliente = cliente
        self.proveedor = proveedor
        self.inventario = inventario
        self.producto = producto
        self.factura = factura
        self.productos = productos

    def agregar_producto(self):
        pass

    def crear_lista(self):
        pass

    def quitar_producto(self):
        pass

    def consultar_productos(self):
        return self.productos
