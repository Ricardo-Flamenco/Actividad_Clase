#X O intento

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")

list_of_victory = 12

while board != list_of_victory:
    turno_x = True
    turno_o = True

    while turno_x:
        row = int(input("Turno X. ingrese fila: [1-3]")) - 1
        if row in [0,1,2]:
                column = int(input("Turno X. ingrese columa: [1-3]")) - 1
                if column in [0,1,2]:
                    break
                else:
                    print("Ingrese numeros del 1 al 3")
        else:
            print("Ingrese numeros del 1 al 3")
    board[row][column] = "X"

    print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")

    while turno_o:
        row = int(input("Turno O. ingrese fila: [1-3]")) - 1
        if row in [0,1,2]:
                column = int(input("Turno O. ingrese columa: [1-3]")) - 1
                if column in [0,1,2]:
                    break
                else:
                    print("Ingrese numeros del 1 al 3")
        else:
            print("Ingrese numeros del 1 al 3")
    board[row][column] = "O"

    print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")