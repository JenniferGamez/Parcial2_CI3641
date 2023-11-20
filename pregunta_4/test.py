# Jennifer Gámez 16-10396
# Pregunta 4: main.py, donde se hace uso de las Implementación  de las subrutinas

from sub_f import F_recursiva, F_recursiva_cola, F_iterativa
import pytest
import unittest

import unittest

class TestFunciones(unittest.TestCase):
    
    # Prueba para F_recursiva con valores conocidos
    def test_F_recursiva(self):
        self.assertEqual(F_recursiva(4, 5, 10), 10)
        self.assertEqual(F_recursiva(3, 6, 20), 24)
        
    # Prueba para F_recursiva_cola con valores conocidos
    def test_F_recursiva_cola(self):
        self.assertEqual(F_recursiva_cola(4, 5, 10, [i for i in range(20)]), 10)
        self.assertEqual(F_recursiva_cola(3, 6, 20, [i for i in range(18)]), 24)

    # Prueba para F_iterativa con valores conocidos
    def test_F_iterativa(self):
        self.assertEqual(F_iterativa(4, 5, 10), 10)
        self.assertEqual(F_iterativa(3, 6, 20), 24)
        
if __name__ == '__main__':
    unittest.main()
