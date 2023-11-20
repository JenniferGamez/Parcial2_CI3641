# Jennifer Gamez
# Pregunta 2: Test del Manejador de operaciones aritmeticas Pre-fijo y Post-fijo

import pytest
import unittest
from unittest.mock import patch
from io import StringIO
from aritmetica import evaluate, to_infix
from main import programa

# Clase de pruebas unitarias
class TestEvaluateFunction(unittest.TestCase):

    # Operaciones Simples POST

    def test_simple_addition_post(self):
        result = evaluate("5 3 +", "POST")
        self.assertEqual(result, 8)  # Verifica si la suma simple funciona

    def test_simple_subtraction_post(self):
        result = evaluate("5 3 -", "POST")
        self.assertEqual(result, 2)  # Verifica si la resta simple funciona

    def test_simple_multiplication_post(self):
        result = evaluate("5 3 *", "POST")
        self.assertEqual(result, 15)  # Verifica si la multiplicación simple funciona

    def test_combination_post(self):
        result = evaluate("8 3 - 8 4 4 + * +", "POST")
        self.assertEqual(result, 69)  # Verifica si se maneja correctamente la combinacion de varios operadores
    
    # Operaciones Simples Pre

    def test_simple_division_pre(self):
        result = evaluate("/ 2 8", "PRE")
        self.assertEqual(result, 4)  # Verifica si la división simple funciona

    def test_division_by_zero_pre_NONE(self):
        result = evaluate("/ 0 2", "PRE")
        self.assertIsNone(result)  # Verifica si se maneja correctamente la división por cero

    def test_division_by_zero_pre(self):
        result = evaluate("/ 2 0", "PRE")
        self.assertEqual(result, 0)  # Verifica si se maneja correctamente la división por cero


    def test_combination_pre(self):
        result = evaluate("+ * + 3 4 5 7", "PRE")
        self.assertEqual(result, 42)  # Verifica si se maneja correctamente la combinacion de varios operadores
    

class TestMain(unittest.TestCase):

    def test_ayuda(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            with patch('builtins.input', side_effect=['AYUDA', 'SALIR']):
                # Simulación del bucle principal con instrucciones simuladas
                programa()
                output = mock_output.getvalue().strip()
                self.assertIn("Instrucciones del programa:", output)  # Verifica si la salida contiene el mensaje de ayuda

    def test_accion_incorrecta(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            with patch('builtins.input', side_effect=['ACCION_INCORRECTA', 'SALIR']):
                programa()
                output = mock_output.getvalue().strip()
                self.assertIn("La  acción debe ser (EVAL <orden> <expr>, MOSTRAR <orden> <expr>, SALIR, AYUDA)", output)  # Verifica si muestra un mensaje de error por acción incorrecta

    def test_mostrar_correcto_post(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            with patch('builtins.input', side_effect=['MOSTRAR POST 8 3 - 8 4 4 + * +', 'SALIR']):
                programa()
                output = mock_output.getvalue().strip()
                self.assertIn("((8 - 3) + (8 * (4 + 4)))", output)  # Verifica si la salida contiene la expresión en notación infija

    def test_mostrar_correcto_pre(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            with patch('builtins.input', side_effect=['MOSTRAR PRE + * + 3 4 5 7', 'SALIR']):
                programa()
                output = mock_output.getvalue().strip()
                self.assertIn("(7 + (5 * (4 + 3)))", output)  # Verifica si la salida contiene la expresión en notación infija

if __name__ == '__main__':
    unittest.main()
