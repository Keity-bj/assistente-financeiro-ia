print("💰 Assistente Financeiro Inteligente")
print("Digite 'sair' para encerrar\n")

while True:

    pergunta = input("Você: ").lower()
    
    with open("historico.txt", "a") as arquivo:
        arquivo.write(pergunta + "\n")

    if pergunta == "sair":
        print("Assistente: Até logo!")
        break

    elif "simular" in pergunta:

        valor = float(input("Digite o valor inicial: "))
        taxa = float(input("Taxa de juros (% ao mês): "))
        meses = int(input("Quantidade de meses: "))

        montante = valor * (1 + taxa/100) ** meses

        print(f"Assistente: Após {meses} meses você terá R${montante:.2f}")

    elif "cdb" in pergunta:
        print("Assistente: CDB é um investimento de renda fixa oferecido por bancos.")

    elif "juros" in pergunta:
        print("Assistente: Juros são a remuneração pelo uso de um dinheiro emprestado.")

    elif "investimento" in pergunta:
        print("Assistente: Investir é aplicar dinheiro esperando retorno futuro.")

    else:
        print("Assistente: Desculpe, ainda não sei responder isso.")