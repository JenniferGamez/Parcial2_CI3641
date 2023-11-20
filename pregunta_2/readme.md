# EXAMEN 2 - CI3641 - PREGUNTA 2
# Jennifer Gámez 16-10396

## Instrucciones de Ejecucion

    - aritmetica.py: Contiene la definición de evaluate; función que evalua las expresiones en post-fijo y pre-fijo según se indique. Tambien contiene la función to_infix que una función que imprime la expresión.
    - main.py: Contiene el main() o la lógica principal de la aplicación.
    - test.py: Contiene las pruebas unitarias.

1. Puede probar el programa, ejecutando la terminal:

    ``` python3 main.py ```

2. Las instrucciones permitidas son: EVAL, MOSTRAR, AYUDA y SALIR.

3. Para ejercutar las pruebbas en Python utilice el marco de prueba

    ``` pytest  ```

4. Para probar la cobertura del programa ejecute

    ``` coverage run -m unittest test.py ```  

5. y si desea mas detalles de cobertura

    ``` coverage report -m  ```
    
6. Instrucciones del programa:

    1. Para evaluar una expresión escriba: EVAL <orden> <expr>"
    Ejemplo: EVAL PRE + * + 3 4 5 7"
    2. Para mostrar una expresión escriba: MOSTRAR <orden> <expr>"
    Ejemplo: MOSTRAR POST 8 3 - 8 4 4 + * +"
    4. Para ver estas instrucciones nuevamente, escriba: AYUDA
    5. Para salir del programa, escriba: SALIR.

## Requisitos del Sistema

Para realizar las pruebas de cobertura, asegúrate de cumplir con los siguientes requisitos:

1. Tener instalado pytest. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

    ``` pip install pytest```

2. Tener instalado coverage. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

    ``` pip install coverage```

Asegúrate de que ambas dependencias estén instaladas y configuradas en tu entorno antes de ejecutar las pruebas de cobertura.
