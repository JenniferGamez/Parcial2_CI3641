# EXAMEN 2 - CI3641 - PREGUNTA 4
# Jennifer Gámez 16-10396

## Instrucciones de Ejecucion.

    - sub_f.py: Contiene la definición de las funciones de recursión:
        - F_recursiva(alpha, beta, n): es una subrutina recursiva
        - F_recursiva_cola(alpha, beta, n, list2, i): es una subrutina recursiva de cola
        - F_iterativa(alpha, beta, n): es una subrutina iterativa de la recursión de cola
        
    - main.py: Contiene el main() o la lógica principal de la aplicación, en este se hace uso de pandas y matplotlib para reflejar los resultados de los datos procesados.
    - test.py: Contiene las pruebas unitarias de sub_f.py

1. Puede probar el programa, ejecutando la terminal:

    ``` python3 main.py ```

El cual tiene asignado procesar quince dato

2. Para ejercutar las pruebas en Python utilice el marco de prueba

    ``` pytest  ```

3. Para probar la cobertura del programa ejecute

    ``` coverage run -m unittest test.py ```  

4. y luego

    ``` coverage report -m  ```
    
6. Instrucciones del programa:

    En sub_f.py , se encuentran las constantas X = 3, Y = 9, Z = 6 que dan valor al alpha y beta, estas pueden ser cambiadas y el programo calcula los nuevos valores para estos. El valor de n se calcula en un rango aleatorio de (50, 100)

## Requisitos del Sistema

Para realizar las pruebas de cobertura, asegúrate de cumplir con los siguientes requisitos:

1. Tener instalado pytest. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

    ``` pip install pytest```

2. Tener instalado coverage. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

    ``` pip install coverage```

Asegúrate de que ambas dependencias estén instaladas y configuradas en tu entorno antes de ejecutar las pruebas de cobertura.