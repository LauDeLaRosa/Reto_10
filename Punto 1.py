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
