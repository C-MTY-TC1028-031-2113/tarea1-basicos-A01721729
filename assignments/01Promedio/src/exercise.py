def main():
    #escribe tu código abajo de esta línea
    materia1 = float(input("Calificacion de la materia: "))
    materia2 = float(input("Calificacion de la materia: "))
    materia3 = float(input("Calificacion de la materia: "))
    materia4 = float(input("Calificacion de la materia: "))

    promedio = (materia1 + materia2 + materia3 + materia4)/4

    print ("Promedio: " + str(promedio))


if __name__ == '__main__':
    main()
