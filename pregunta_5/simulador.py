# Jennifer Gamez
# Pregunta 5: Simulador de Manejador de Tipo de Datos

class AtomicType:
    def __init__(self, name, representation, alignment):
        self.name = name
        # Ajusta el tamaño y la alineación para que sean múltiplos de 2
        self.representation = 2 ** (representation.bit_length() - 1)
        self.alignment = 2 ** (alignment.bit_length() - 1)

def calculate_size_alignment(fields):
    max_size = 0
    max_alignment = 2  

    for field in fields:
        if field in types and isinstance(types[field], AtomicType):
            max_size = max(max_size, types[field].representation)
            max_alignment = max(max_alignment, types[field].alignment)

    # Ajusta el tamaño para que sea múltiplo de la alineación
    size = ((max_size + max_alignment - 1) // max_alignment) * max_alignment
    alignment = max_alignment

    return size, alignment

class StructType:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.calculate_size_alignment()

    def calculate_size_alignment(self):
        self.size, self.alignment = calculate_size_alignment(self.fields)

class UnionType:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.calculate_size_alignment()

    def calculate_size_alignment(self):
        self.size, self.alignment = calculate_size_alignment(self.fields)


# Diccionario para almacenar los tipos definidos
types = {}

def define_atomic(name, representation, alignment):
    if name in types:
        print(f"Error: El tipo '{name}' ya ha sido definido.")
        return
    
    # Ajusta el tamaño y la alineación para que sean múltiplos de 2
    representation = 2 ** (representation.bit_length() - 1)
    alignment = 2 ** (alignment.bit_length() - 1)
    
    types[name] = AtomicType(name, int(representation), int(alignment))
    print(f"Tipo atómico '{name}' definido con representación {representation} bytes y alineación {alignment} bytes.")

def define_struct(name, fields):
    if name in types:
        print(f"Error: El tipo '{name}' ya ha sido definido.")
        return

    for field in fields:
        if field not in types:
            print(f"Error: El tipo '{field}' no ha sido definido.")
            return
    
    types[name] = StructType(name, fields)
    print(f"Struct '{name}' definido con campos {fields}.")

def define_union(name, fields):
    if name in types:
        print(f"Error: El tipo '{name}' ya ha sido definido.")
        return

    combined_fields = []
    for field in fields:
        if field not in types:
            print(f"Error: El tipo '{field}' no ha sido definido.")
            return
        combined_fields.append(types[field])  # Agregar el tipo al campo combinado
    
    types[name] = UnionType(name, combined_fields)
    print(f"Union '{name}' definido con campos {fields}.")

def describe_type(name):
    if name not in types:
        print(f"Error: El tipo '{name}' no ha sido definido.")
        return

    if isinstance(types[name], AtomicType):
        print(f"Tipo Atómico '{name}':")
        print(f"Tamaño: {types[name].representation} bytes")
        print(f"Alineación: {types[name].alignment} bytes")

    elif isinstance(types[name], StructType):
        print(f"Struct '{name}':")
        print(f"Campos originales: {types[name].fields}")
        fields_sorted = sorted(types[name].fields, key=lambda x: (types[x].alignment, types[x].representation), reverse=True)
        print(f"Campos reordenados: {fields_sorted}")

    elif isinstance(types[name], UnionType):
        print(f"Union '{name}':")
        print(f"Campos originales: {types[name].fields}")
        fields_sorted = sorted(types[name].fields, key=lambda x: (types[x].alignment, types[x].representation), reverse=True)
        print(f"Campos reordenados: {fields_sorted}")
        
def programa():
    print("Simulador de manejador Tipos de Datos.")
    print("Ingrese una acción (ATOMICO, STRUCT, UNION, DESCRIBIR, SALIR): ")
    while True:
        linea = input("> ")
        instruccion = linea.split()
        
        if instruccion[0].upper() == "ATOMICO":
            define_atomic(instruccion[1], int(instruccion[2]), int(instruccion[3]))
        elif instruccion[0].upper() == "STRUCT":
            define_struct(instruccion[1], instruccion[2:])
        elif instruccion[0].upper() == "UNION":
            define_union(instruccion[1], instruccion[2:])
        elif instruccion[0].upper() == "DESCRIBIR":
            describe_type(instruccion[1])
        elif instruccion[0].upper() == "SALIR":
            break
        else:
            print("Acción no válida. Intente de nuevo.")

# Ejecutar el bucle principal
if __name__ == "__main__":
    programa()