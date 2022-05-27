
class Cliente:
    def __init__(self, nombre, apellido, contacto, direccion, deudas):
        self.nombre = nombre
        self.apellido = apellido
        self.contacto = contacto
        self.direccion = direccion
        self.deudas = deudas

    def hacer_reclamacion(self):
        print("\t1. Pedido incompleto.\n\t2. Pedido diferente.\n\t3. Pedido no entregado.")
        tipo = int(input("Ingrese una opción: "))
        while tipo < 1 or tipo > 3:
            tipo = int(input("Elija una opción válida: "))
        if tipo == 3:
            reclamo = "El pedido no se entregó."
        else:
            reclamo = input("Brinde más información de lo sucedido: \n")
        return reclamo

    def hacer_sugerencia(self):
        sugerencia = input("Díganos sus comentarios para mejorar: \n")
        return sugerencia

    def pedir_domicilio(self):
        print("\t1. Pedir a domicilio.\n\t2. Recoger en tienda.")
        domicilio = int(input("Ingrese una opción: "))
        while domicilio < 1 or domicilio > 2:
            domicilio = int(input("Elija una opción válida: "))
        if domicilio == 1:
            return True
        else:
            return False
    def comprar(self, producto, cantidad):
        if Inventario.pedido_producto(producto, cantidad):
            return "Pedido creado."
        return "Existencias insuficientes."
