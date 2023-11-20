package main

import (
    "fmt"
    "sync"
)

func esPrimo(numero int) bool {
    if numero <= 1 {
        return false
    }
    for i := 2; i*i <= numero; i++ {
        if numero%i == 0 {
            return false
        }
    }
    return true
}

func encontrarPrimos(inicio, fin int, wg *sync.WaitGroup) {
    defer wg.Done()
    for i := inicio; i <= fin; i++ {
        if esPrimo(i) {
            fmt.Printf("%d es primo\n", i)
        }
    }
}

func main() {
    limiteSuperior := 100
    numGoroutines := 4
    var wg sync.WaitGroup

    for i := 0; i < numGoroutines; i++ {
        wg.Add(1)
        segmento := limiteSuperior / numGoroutines
        inicio := i * segmento
        fin := (i+1)*segmento - 1
        go encontrarPrimos(inicio, fin, &wg)
    }

    wg.Wait()
}
