package main

import "fmt"

func divide(a, b int) int {
    if b == 0 {
        panic("División por cero no permitida")
    }
    return a / b
}

func main() {
    numerador := 10
    denominador := 0

    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recuperado de un pánico:", r)
        }
    }()

    resultado := divide(numerador, denominador)
    fmt.Println("Resultado:", resultado)
}
