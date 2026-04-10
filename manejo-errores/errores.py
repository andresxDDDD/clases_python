
#error
#try y el except



try:  #intenta ejecutar esto
    lista = [1,2,3,4,5,6,7,8]
    print(lista[20])
except IndexError: # si el bloque anterior de try tiene errores  esto captura el error especifico lo muestra en pantalla cli y continua con la ejecucion
     print(f"indice fuera de rango")


try:
    a = int(input("ingresa un numero:"))
    b = int(input("ingrese un numero:")) 
    resultado = a/b
    print(resultado)
except SyntaxError:
    print("error de sistaxis en python")
except ValueError:
    print("solo numeros plz")
except ZeroDivisionError:
    print("no se puede  dividir por 0 plz")





    











