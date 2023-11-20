# Jennifer Gámez 16-10396
# Pregunta 4: Implementación  de las subrutinas

# A: Subrutina recursiva
def F_recursiva(alpha, beta, n):
    if -1 < n < alpha * beta:
        return n
    elif n >= alpha * beta:
        return sum(F_recursiva(alpha, beta, n - beta * i) for i in range(1, alpha+1))

# B : Subrutina Recursiva de Cola
def F_recursiva_cola(alpha, beta, n, list2, i=0):
    if -1 < n < alpha * beta:
        return list2[n+i]

    elif n >= alpha*beta:
        lista = sum([list2[j+i] for j in range(0, alpha*beta, beta)])
        list2.append(lista)
        return F_recursiva_cola(alpha, beta, n-1, list2, i+1)

# C : Subrutina Iterativa
def F_iterativa(alpha, beta, n):
    list2 = [i for i in range(0,alpha*beta)]
    
    if -1 < n < alpha * beta:
        return n
    
    elif n >= alpha * beta:
        for j in range(alpha*beta, n+1): # Se cambia la recursión por una iteración
            i = j-alpha * beta
            lista = sum([list2[j+i] for j in range(0, alpha * beta, beta)])
            list2.append(lista)
            n -= 1
        
        return list2[len(list2)-1]