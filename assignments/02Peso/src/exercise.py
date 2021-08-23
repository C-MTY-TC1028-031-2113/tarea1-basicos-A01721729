def main():
    #escribe tu código abajo de esta línea
    pesoInicial = float(input("Peso inicial: "))
    pesoFinal = float(input("Peso final: "))
    tiempoMeses = int(input("Dame el tiempo en meses: "))
    pesoBajar = (pesoInicial - pesoFinal)/2

    print("Lo que debes bajar por mes es: " + str(pesoBajar) + "Kg al mes")

if __name__ == '__main__':
    main()
