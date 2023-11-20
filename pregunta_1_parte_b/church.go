// Jennifer Gamez 16-10396
// Numeros de Church
package main

import "fmt"

// Definimos el tipo de dato Church
type Church struct {
	number *Church
}

// Definimos la función sucesor de un numero Church
func Suc(n *Church) *Church {
	return &Church{n}
}

// Función para representar el número cero en la notación de Church
func Zero() *Church {
	return &Church{nil}
}

// Función para convertir un entero a su representación en la notación de Church
func IntToChurch(n int) *Church {
	churchNum := Zero()

	for i := 0; i < n; i++ {
		churchNum = Suc(churchNum)
	}

	return churchNum
}

// Función para convertir un número de Church a entero
func ChurchToInt(churchNum *Church) int {
	count := 0
	curr := churchNum

	for curr.number != nil {
		count++
		curr = curr.number
	}

	return count
}

// Función para sumar dos números de Church
func Sum(numA, numB *Church) *Church {
	if numA == nil {
		return numB
	}
	return Suc(Sum(numA.number, numB))
}

// Función para multiplicar dos números de Church
func Multiply(numA, numB *Church) *Church {
	if numA == nil || numB == nil {
		return &Church{nil}
	}
	return mult(numA, numB, Zero())
}

// Función auxiliar para la multiplicación de dos números de Church
func mult(a, b, acc *Church) *Church {
	if b == nil {
		return acc
	}
	return mult(a, b.number, Sum(acc, a))
}


func main() {
	// Generamos varios numerales de Church
	numeroCero := Zero()
	numeroUno := Suc(Zero())
	numeroDos := Suc(Suc(Zero()))
	numeroTres := Suc(numeroDos)

	// Calcular el sucesor de un número entero
	numeroEntero := 5 
	numChur:= IntToChurch(numeroEntero)
	sucesor := Suc(numChur)
	
	sum_resultado := Sum(numeroDos, sucesor)
	mult_resultado := Multiply(numeroDos, numeroTres)
	
	// Verificamos si representan los números 0, 1, 2
	fmt.Println("Representación del cero: ", ChurchToInt(numeroCero)) // Imprime 0
	fmt.Println("x = ", ChurchToInt(numeroUno))    // x = 1
	fmt.Println("y = ", ChurchToInt(numeroDos))    // y = 2
	fmt.Println("q = ", ChurchToInt(numeroTres))    // y = 2
	fmt.Println("Sucesor de un numero intero, z =", ChurchToInt(sucesor)) // numeroEntero = 5.suc = 6
	fmt.Println("z + x =", ChurchToInt(sum_resultado)) // suma de 5.suc() + y = 8 
	fmt.Println("El resultado de la multiplicación es:", ChurchToInt(mult_resultado))
}
