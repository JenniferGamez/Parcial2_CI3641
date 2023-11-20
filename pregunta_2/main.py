# Jennifer Gamez
# Pregunta 2: Manejador de operaciones aritmeticas Pre-fijo y Post-fijo

from aritmetica import (
    evaluate,
    to_infix,
)

def programa():
    print("Manejador operaciones aritmeticas en orden: Pre-fijo y Post-fijo.")
    print("Ingrese una acción (EVAL <orden> <expr>, MOSTRAR <orden> <expr>, SALIR, AYUDA): ")

    while True:
        
        linea = input("> ")
        instruccion = linea.split()
        
        if instruccion[0].upper() == 'EVAL':
            order = instruccion[1]
            expr = ' '.join(instruccion[2:])
            result = evaluate(expr, order)
            if result is not None:
                print(result)
        
        elif instruccion[0].upper() == 'MOSTRAR':
            order = instruccion[1]
            expr = ' '.join(instruccion[2:])
            result = to_infix(expr, order)
            if result is not None:
                print(result)
        
        elif instruccion[0].upper() == 'SALIR':
            break

        elif instruccion[0].upper() == 'AYUDA':
            print("Instrucciones del programa:")
            print("1. Para evaluar una expresión escriba: EVAL <orden> <expr>")
            print("   Ejemplo: EVAL PRE + * + 3 4 5 7")
            print("2. Para mostrar una expresión escriba: MOSTRAR <orden> <expr>")
            print("   Ejemplo: MOSTRAR POST 8 3 - 8 4 4 + * +")
            print("5. Para salir del programa, escriba: SALIR.\n")

        else:
            print("La  acción debe ser (EVAL <orden> <expr>, MOSTRAR <orden> <expr>, SALIR, AYUDA)")

# Ejecutar el bucle principal
if __name__ == "__main__":
    programa()