
import sys
import pandas as pd

# Comprobar la versión de Python
print("Versión de Python:", sys.version.split()[0])

# Crear una tabla sencilla de ventas
datos = {
    "Producto": ["Camisetas", "Pantalones", "Tenis"],
    "Ventas": [30000, 42500, 180000]
}

df = pd.DataFrame(datos)

# Mostrar los resultados
print("\nTabla de ventas:")
print(df)

print("\nProducto con mayores ventas:")
print(df.loc[df["Ventas"].idxmax(), "Producto"])
