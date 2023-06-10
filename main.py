
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
import os


# funciones
def MuestraTitulo ():
    if os.name == "posix":
        var = "clear"       
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    os.system(var)
    tittle = "  _____                        .__  .__                     .__   \n_/ ____\_ __  ____             |  | |__| ____   ____ _____  |  |  \n\   __\  |  \/    \    ______  |  | |  |/    \_/ __ \ \__ \ |  |  \n |  | |  |  /   |  \  /_____/  |  |_|  |   |  \  ___/ / __ \|  |__\n |__| |____/|___|  /           |____/__|___|  /\___  >____  /____/\n                 \/                         \/     \/     \/      "
    print(tittle)

def linearFuntion(dependiente = 1, independiente = 0):
    x = list(range (-2, 3, 1))
    y = list (map(lambda x : (x* dependiente + independiente), x))
    tabla =  list(zip(x,y))
    MuestraTitulo()
    print('\nValores de coordenadas')
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

def MuestraMenu():
    menu = f"1: salir \n\r2: funcion lineal"
    print(menu)


# main

while (True):
    MuestraTitulo()
    MuestraMenu()

    option = int(input("==>  "))
    


    if option == 1:
        break
    elif option == 2:
        
        try:
            MuestraTitulo()
            a = int(input('favor de ingresar la variable dependiente:  '))
            b = int(input('favor de ingresar la variable independiente:  '))
            linearFuntion(a, b)
        except:
            print('Sintax Err')
            input('enter para continuar')
    else:
        print('Error')
        input('enter para continuar')