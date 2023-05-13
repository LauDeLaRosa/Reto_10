def calcular_producto_punto(arreglo1, arreglo2):
    producto_punto = 0
    for i in range(len(arreglo1)):
        producto_punto += arreglo1[i] * arreglo2[i]
    return producto_punto
if __name__ == "__main__":
 arreglo1_ejemplo = [1, 2, 3, 4, 5]
 arreglo2_ejemplo = [7, 10, 34, 56, 65]
producto_punto = calcular_producto_punto(arreglo1_ejemplo, arreglo2_ejemplo)
print(producto_punto)
