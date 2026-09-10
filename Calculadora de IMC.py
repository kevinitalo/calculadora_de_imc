# calculadora de IMC
while True:
    peso = input("peso (kg): ")

    if "," in peso:
        peso = peso.replace(",", ".")
    peso = float(peso)

    while peso <= 0:
        print("Peso inválido. Por favor, insira um valor maior que zero.")
        peso = input("peso (kg): ")
        if "," in peso:
            peso = peso.replace(",", ".")
        peso = float(peso)

    altura = float(input("altura (m): "))

    while altura <= 0:
            print("Altura inválida. Por favor, insira um valor maior que zero.")
            altura = float(input("altura (m): "))

    imc = peso / (altura ** 2)
    print(f"IMC: {imc:.1f}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso normal")
    elif imc < 30:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")

    tecla = input("Pressione a tecla 'X' para sair...")
    if tecla.upper() == 'X':
        break