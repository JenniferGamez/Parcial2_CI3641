# Jennifer Gamez
# Pregunta 3 b

def incremento_list(p): 
    if p == []: 
        yield [] 
    else: 
        for x in incremento_list(p[1:]): 
            yield x 
            if x==[] or p[0]<= x[0]: 
                yield [p[0], *x] 
 
for x in incremento_list([1,4,3,2,5]): 
    print(x)    
    