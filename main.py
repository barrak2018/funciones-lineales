
# Programación Númerica y No Númerica DCN-501

# Jorge Polo
# C.I: V-18.587.447

# Gustavo Hernández
# C.I: V-28.317.635

# Jose Ojeda
# C.I: V-29.845.213

# Leonardo Yanez
# C.I: V-30.300.275
import matplotlib.pyplot as pp

# funciones
def MuestraTitulo ():
    print ("")

def linearFuntion(dependiente = 1, independiente = 0):
    x = list(range (-2, 3, 1))
    y = list (map(lambda x : (x* dependiente + independiente), x))
    tabla =  list(zip(x,y))
    for index, tupla in enumerate (tabla):
        a, b = tupla 
        print(f"{index+1}: X= {a} Y= {b}")
    print (x, y)
    pp.plot(x, y)
    pp.show()



# main

linearFuntion(9,12)
