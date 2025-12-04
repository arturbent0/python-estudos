nome_arquivo = input("Digite o nome do arquivo para armazenar as palavras: ")

with open(nome_arquivo, 'w') as arq:
    while True:
        palavra = input("Digite a palavra (ou \exit para sair): ")

        if palavra == "\exit":
            break

        arq.write(f"{palavra}\n")

print("Palavras armazenadas")

with open(nome_arquivo, 'r') as arq:
    conteudo = arq.read()
    print(conteudo)

valores = [1,2,3,4,5]

with open('valores.txt', 'w') as arq:
    for valor in valores:
        arq.write(str(valor) + '\n')

with open('valores.txt', 'a') as arq:
    for valor in valores:
        arq.write(str(valor) + '\n')

with open('valores.txt', 'r') as arq:
    for valor in arq:
        print(valor)