def create_token_table(text):
    lines = text.split('\n')
    token_table = {}

    row = 0
    col = 0

    for line in lines:
        tokens = line.split()
        for token in tokens:
            token = token.replace(' ', '')  # Eliminar espacios en blanco del token
            if token:  # Ignorar tokens vacíos
                token_table[(row, col)] = token
                col += len(token)  # No se agrega +1 para el espacio entre tokens

                if col >= len(line):
                    col = 0
                    row += 1
                else:
                    col += 1

        col = 0  # Reset column position after each line

    return token_table


def search_token(token_table, row, col):
    return token_table.get((row, col), None)


# Ejemplo de uso
print("Ingresa la sintaxis de C++ (puedes realizar saltos de línea). Escribe 'fin' en una línea separada para terminar.")

lines = []
while True:
    line = input()
    if line == "fin":
        break
    lines.append(line)

code = '\n'.join(lines)

table = create_token_table(code)

print("Tabla de tokens:")
for position, token in table.items():
    print(f'{position}: {token}')

search_option = input("¿Deseas buscar un token en la tabla hash? (s/n): ")
if search_option.lower() == 's':
    search_row = int(input("Ingresa la fila: "))
    search_col = int(input("Ingresa la columna: "))

    search_result = search_token(table, search_row, search_col)
    if search_result:
        print(f"Token encontrado: {search_result}")
    else:
        print("Token no encontrado.")




