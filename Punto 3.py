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
