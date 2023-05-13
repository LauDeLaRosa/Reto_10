# Reto 10 sin fuerzas para uno más
## Ejercicio #1
Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
def calcular_promedio(arreglo): #Se define la funcion
    suma = 0.0 
    for x in arreglo:
        suma += x #Se define la suma de los elementos
    promedio = suma / len(arreglo) #Se define el calculo del promedio
    return promedio
if __name__ == "__main__":
 arreglo_ejemplo = [1.4, 5.6, 7.8, 9.4, 344.5, 56.9] #Un ejemplo de arreglo de reales
promedio = calcular_promedio(arreglo_ejemplo) #Se determina el calculo del promedio con los argumentos que tenemos
print(promedio) #Se imprime el resultado
```

## Ejercicio #2
Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
```python
def calcular_producto_punto(arreglo1, arreglo2):#Se define la funcion
    producto_punto = 0
    for i in range(len(arreglo1)):
        producto_punto += arreglo1[i] * arreglo2[i] #Se define el producto punto
    return producto_punto
if __name__ == "__main__":
 #Se definen los ejemplos de arreglos
 arreglo1_ejemplo = [1, 2, 3, 4, 5] 
 arreglo2_ejemplo = [7, 10, 34, 56, 65]
producto_punto = calcular_producto_punto(arreglo1_ejemplo, arreglo2_ejemplo) #Se pide la funcion y se calcula
print(producto_punto) #Se imprime el resultado
```

## Ejercicio #3
Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```python
def mover_ceros_al_final(arreglo):#Se define la funcion
    ultimo_cero = 0
    for i in range(len(arreglo)):
        if arreglo[i] != 0:
            arreglo[ultimo_cero], arreglo[i] = arreglo[i], arreglo[ultimo_cero]
            ultimo_cero += 1
    return arreglo
if __name__ == "__main__":
 arreglo_ejemplo = [20, 0, 35, 0, 10, 24, 0, 40, 55, 0] #Se pone el ejemplo de arreglo
 arreglo_resultante = mover_ceros_al_final(arreglo_ejemplo) #Se pide la funcion
print(arreglo_resultante) #Se imprime el resultado
```
