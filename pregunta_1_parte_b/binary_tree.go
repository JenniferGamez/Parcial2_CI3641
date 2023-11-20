// Jennifer Gamez 16-10396
// Numeros de Church

package main

import (
	"fmt"
	"strings"
)

// Definición de la estructura del árbol binario
type Arbol struct {
	Valor       int
	Izquierda   *Arbol	// Nodo hijo izquierdo
	Derecha     *Arbol	// Nodo hijo derecho
}

// Función para verificar si es un max-heap simétrico
func esMaxHeapSimetrico(arbol *Arbol) bool {
	esMAxHeap := isEqual(preOrder(arbol), reverse(postOrder(arbol)))

	if esMAxHeap {
		fmt.Println("El árbol es un max-heap simétrico.")
		return true
	} else {
		fmt.Println("El árbol no es un max-heap simétrico.")
		return false
	}
}

// Función para recorrido en pre-orden
func preOrder(arbol *Arbol) []int {
	if arbol == nil {
		return []int{}
	}
	result := []int{arbol.Valor}
	result = append(result, preOrder(arbol.Izquierda)...)
	result = append(result, preOrder(arbol.Derecha)...)
	return result
}

// Función para recorrido en post-orden
func postOrder(arbol *Arbol) []int {
	if arbol == nil {
		return []int{}
	}
	result := postOrder(arbol.Izquierda)
	result = append(result, postOrder(arbol.Derecha)...)
	result = append(result, arbol.Valor)
	return result
}

// Función para revertir un slice de enteros
func reverse(s []int) []int {
	length := len(s)
	reversed := make([]int, length)
	for i, v := range s {
		reversed[length-i-1] = v
	}
	return reversed
}

// Función para verificar si dos slices son iguales
func isEqual(s1, s2 []int) bool {
	if len(s1) != len(s2) {
		return false
	}
	for i, v := range s1 {
		if v != s2[i] {
			return false
		}
	}
	return true
}

// Función para imprimir el árbol 
func imprimirArbol(arbol *Arbol, espacio int) {
	if arbol == nil {
		return
	}

	espacio += 7 // Ajusta el espaciado para niveles diferentes

	imprimirArbol(arbol.Derecha, espacio)

	fmt.Println(strings.Repeat(" ", espacio), arbol.Valor)

	imprimirArbol(arbol.Izquierda, espacio)
}


func main() {
	// Creación del árbol binario
	arbol1 := &Arbol{
		Valor: 1,
		Izquierda: &Arbol{
			Valor: 2,
			Izquierda: &Arbol{
				Valor: 4,
			},
			Derecha: &Arbol{
				Valor: 5,
			},
		},
		Derecha: &Arbol{
			Valor: 3,
			Izquierda: &Arbol{
				Valor: 6,
			},
			Derecha: &Arbol{
				Valor: 7,
			},
		},
	}

	// Verificar si el árbol es un max-heap simétrico
	imprimirArbol(arbol1, 0)
	esMaxHeapSimetrico(arbol1)

	arbol2 := &Arbol{
		Valor: 6,
		Izquierda: &Arbol{
			Valor: 2,
			Izquierda: &Arbol{
				Valor: 1,
			},
			Derecha: &Arbol{
				Valor: 3,
			},
		},
		Derecha: &Arbol{
			Valor: 2,
			Izquierda: &Arbol{
				Valor: 3,
			},
			Derecha: &Arbol{
				Valor: 1,
			},
		},
	}

	// Verificar si el árbol es un max-heap simétrico
	imprimirArbol(arbol2, 0)
	esMaxHeapSimetrico(arbol2)
}