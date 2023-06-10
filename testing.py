import matplotlib.pyplot as pp


def quadraticFunction (cuadratico, lineal, independiente):
    x = list(range(-100, 100, 1))
    #print(x)
    y = list (map(lambda x : ( (cuadratico * pow(x,2)) + (lineal * x) + independiente ), x))
    #print(y)
    tabla = (zip(x,y))

    #MuestraTitulo()

    #print(tabla)
    for index, tupla in enumerate (tabla):
        a, b = tupla 
        print(f"{index+1}: X= {a} Y= {b}")
    pp.plot(x, y)
    pp.xlabel("eje X")
    pp.ylabel('eje Y')
    pp.title("funcion lineal")
    pp.grid()
    print('cerrar grafica para terminar')
    pp.show()
    input('pulse enter para continuar')



quadraticFunction(1, 6, 9) 