from Producto import Producto


class Inventario:
    def __init__(self):
        self.inventario = []

    def existencias(self):
        for i in self.inventario:
            print(i.producto)

    def ingresar_producto(self, producto):
        self.inventario.append(producto)
        return "Producto añadido."

    def eliminar_producto(self, producto):
        cont = 0
        for prod in self.inventario:
            if prod.producto == producto:
                self.inventario.pop(cont)
            cont += 1
        return "Producto eliminado."

    def consultar_prodcuto(self, producto):
        for prod in self.inventario:
            if prod.producto == producto:
                return True
        return False

    def consultar_cantidad(self, producto):
        for prod in self.inventario:
            if prod.producto == producto:
                return prod.cantidad
        return 0

    def pedido_producto(self, producto, cantidad):
        if self.consultar_prodcuto(producto):
            if cantidad <= self.consultar_cantidad(producto):
                return "El pedido se puede realizar."
        return "El pedido no se puede realizar."


inventario = Inventario()
inventario.ingresar_producto(Producto("champú", 100))
inventario.ingresar_producto(Producto("Papa", 50))
inventario.ingresar_producto(Producto("Arroz", 100))
print(inventario.pedido_producto("Papa", 50))

