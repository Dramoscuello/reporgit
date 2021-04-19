def funcone():
    tope = int(input("Dijite el limite: "))
    suma = 0
    for i in range(1, tope+1):
        suma = suma + i
    return suma/tope

def eje2():
    tope = int(input("Dijite el limite: "))
    suma = 0
    if tope % 2 != 0:
        return round(tope/2) + 1
    else:
        for i in range(1, tope+1):
            suma = suma + i
        return suma/tope

def eje3():
    tope = int(input("Dijite el limite: "))
    suma = 0
    if tope % 2 != 0:
        return round(tope/2) + 1
    else:
        for i in range(1, tope+1):
            suma = suma + i
        return suma/tope
        


if __name__ == '__main__':
    #print("La media es: " + str(eje1()))
    #print("La mediana es: " + str(eje2()))
    #1,2,3,4,5,6,7,8,9,10

    es_par = lambda x: x % 2 == 0
    print(es_par(7))

    es_impar = lambda x: x % 2 != 0
    print(es_impar(5))