#X O intento

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

list_of_victory = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],

    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],

    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]

def reset():

    global board
    
    board = [
                        ["", "", ""],
                        ["", "", ""],
                        ["", "", ""]
                    ]
    print("\nTablero reiniciado")
    print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")


def check_win(teams):

    global board
    for combinacion in list_of_victory:
        if all(board[row][column] == teams for row, column in combinacion):
            print(f"=====Ganó={teams}=Tablero=reestablecido=====")
            board = [
                        ["", "", ""],
                        ["", "", ""],
                        ["", "", ""]
                    ]
            print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")


print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")

while board != list_of_victory:
    turno_x = True
    turno_o = True

    while turno_x:
        row = input("Turno X. ingrese fila: [1-3][R para reiniciar]")
        if row.lower() == "r":
            reset()
        else:
            if row.isdigit():
                row = int(row) - 1
                if row in [0,1,2]:
                        column = input("Turno X. ingrese columa: [1-3][R para reiniciar]")
                        if column.lower() == "r":
                            reset()
                        else:
                            if column.isdigit():
                                column = int(column) - 1
                                if column in [0,1,2]:
                                    if board[row][column] == "":
                                        board[row][column] = "X"
                                        break
                                    else:
                                        print("Casilla ocupada")
                                        print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")
                                else:
                                    print("Ingrese numeros del 1 al 3")
                            else:
                                print("Ingrese numeros del 1 al 3")
                else:
                    print("Ingrese numeros del 1 al 3")
            else:
                print("Ingrese numeros del 1 al 3")

    print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")
    check_win("X")

    while turno_o:
        row = input("Turno O. ingrese fila: [1-3][R para reiniciar]")
        if row.lower() == "r":
            reset()
        else:
            if row.isdigit():
                row = int(row) - 1
                if row in [0,1,2]:
                        column = input("Turno O. ingrese columa: [1-3][R para reiniciar]")
                        if column.lower() == "r":
                            reset()
                        else:
                            if column.isdigit():
                                column = int(column) - 1
                                if column in [0,1,2]:          
                                    if board[row][column] == "":
                                        board[row][column] = "O"
                                        break
                                    else:
                                        print("Casilla ocupada")
                                        print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")       
                                else:
                                    print("Ingrese numeros del 1 al 3")
                            else:
                                    print("Ingrese numeros del 1 al 3")
                else:
                    print("Ingrese numeros del 1 al 3")
            else:
                print("Ingrese numeros del 1 al 3")

    print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")
    check_win("O")