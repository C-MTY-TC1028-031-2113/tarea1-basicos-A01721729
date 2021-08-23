def main():
    #escribe tu código abajo de esta línea
    #Lee los datos
    X1 = float(input("Dame X1: "))
    Y1 = float(input("Dame Y1: "))
    X2 = float(input("Dame X2: "))
    Y2 = float(input("Dame Y2: "))

    m = (Y2 - Y1)/(X2 - X1)

    print("Pendiente: " + str(m))



if __name__ == '__main__':
    main()
