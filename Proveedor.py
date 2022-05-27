
class Proveedor:
    def __init__(self, empresa, contacto, direccion, producto, nombre, codigo):
        self.empresa = empresa
        self.contacto = contacto
        self.direccion = direccion
        self.producto = producto
        self.nombre = nombre
        self.codigo = codigo

    def venta(self):
        pass

    def consultar_producto(self):
        return self.producto

    def informar_precios(self):
        return self.producto.precio

    def factura_tienda(self):
        pass

    def entregar_productos(self):
        pass

    def registrar_productos_vendidos(self):
        pass
