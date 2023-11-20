package main
import "fmt"

// Estructura de selección simple

// Estructura de control de flujo condicional de if y else
func condicional() {
    encendido := false
    if encendido {
        fmt.Println("Está encendido")
    } else {
        fmt.Println("Está apagado")
    }
}

// Estructura de control de flujo condicional de else-if
func condicionalElseIf(){
	edad := 180
	if edad > 150 {
		fmt.Println("¿Eres inmortal?")
	} else if edad >= 18 {
		fmt.Println("Eres mayor de edad")
	} else {
		fmt.Println("Eres menor de edad")
	}
}

// Estructura de selección múltiple
func seleccionMultipleBasico(dias int) {
	// dias es el parametro condición a evaluar en el switch
    switch dias {
    case 0:
        fmt.Println("Lunes")
    case 1:
        fmt.Println("Martes")
    case 2:
        fmt.Println("Miercoles")
    case 3:
        fmt.Println("Jueves")
    case 4:
        fmt.Println("Viernes")
    case 5:
        fmt.Println("Sabado")
    case 6:
        fmt.Println("Domingo")
    default:
        fmt.Println("Desconocido")
    }
}

// Estructura de selección múltiple
func seleccionMultiple(edad int) {
	// dias es el parametro condición a evaluar en el switch
    switch {
	case edad > 150:
		fmt.Println("¿Eres inmortal?")
	case edad >= 18:
			fmt.Println("Eres mayor de edad")
	default:
		fmt.Println("Eres menor de edad")
	}
}

// Repetición
func repeticion() {
    for i := 0; i < 10; i++ {
        fmt.Println(i)
    }
}

// Repetición indefinida
func repeticionInd() {
    for {
        fmt.Println("Hola")
    }
}

// 2da estructura de repeticion
func rango(){
    numeros := []int{1, 2, 3, 4, 5}
    for indice, valor := range numeros {
        fmt.Printf("Índice: %d, Valor: %d\n", indice, valor)
    }
}

// Estructura de abstracción procedural

func suma(a int, b int) int {
    resultado := a + b
    return resultado
}


// Estructura de abstracción procedural

// Def del tipo (estructura) Rectangulo
type Rectangulo struct {
    Largo  int	// Campo público
    Ancho  int	// Campo público
}

// METODO "Area" asociado a "Rectangulo" <- Estructura de abstracción procedural
func (r Rectangulo) Area() int {
    return r.Largo * r.Ancho
}


// Recursión

func fibonacci(n int, a, b int) int {
    if n == 0 {
        return a
    }
    if n == 1 {
        return b
    }
    return fibonacci(n-1, b, a+b)
}


func main() {
    fmt.Println("Primera línea") // Se ejecuta primero
    fmt.Println("Segunda línea") // Se ejecuta a continuación
    fmt.Println("Tercera línea") // Se ejecuta después de la segunda línea

	// Estructura de selección
	dia := 1 
	edad := 180
	condicional()
	condicionalElseIf()
	seleccionMultipleBasico(dia)
	seleccionMultiple(edad)

	// Estructura de repetición
	repeticion()
    rango()

	// Forma de uso del metodo de abstracción 

	miRectangulo := Rectangulo{Largo: 5, Ancho: 3}
	area := miRectangulo.Area()
	fmt.Println("El área del rectángulo es:", area)

	// Uso de recursión

	n := 10 
	fmt.Printf("Fibonacci de los primeros 10: ")
    for i := 0; i < n; i++ {
		fmt.Printf("%d ", fibonacci(i, 0, 1))
    }

}
