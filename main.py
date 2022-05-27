
from Proveedor import Proveedor
from Producto import Producto

mani = Producto("mani", 1000, 0.19, 1, "4/29/2022", "No", "Sí")
Juan = Proveedor("Luker", "a", "A", mani, "Juan", 1)

print(Juan.informar_precios())
