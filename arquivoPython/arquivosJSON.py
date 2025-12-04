import json

#json.load() Lê JSON de um arquivo e converte para Python
#json.loads() Lê JSON de uma string e converte para Python
#json.dump() Escreve um objeto Python em um arquivo no formato JSON
#json.dumps() Converte um objeto Python em uma STRING JSON

json_string = """{
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "profissao": "Engenheiro"
}"""

#dados = json.loads(json_string)
#print(dados)
#print(dados['cidade'])

json_string2 = """{
    "livros": [
        {
            "titulo": "A Revolução dos Bichos",
            "autor": "George Orwell",
            "ano_publicacao": 1945,
            "genero": "Ficção política",
            "editora": "Companhia das Letras"
        },
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "ano_publicacao": 1949,
            "genero": "Ficção distópica",
            "editora": "Companhia das Letras"
        }
    ]
}"""

dados1 = json.loads(json_string2)
#print(dados)

for livro in dados1['livros']:
    #print(livro)
    titulo = livro['titulo']
    autor = livro['autor']
    #print(f"Nome: {titulo}\nAutor: {autor}")

frutas = {
    'frutas':[
        {
            'nome': 'maçã',
            'preco': '2.50'
        },
        {
            'nome': 'banana',
            'preco': '3.00'
        }
    ]
}

with open('frutas.json', 'w', encoding='utf-8') as arq:
    json.dump(frutas, arq, indent=4, ensure_ascii=False)

with open('frutas.json', 'r', encoding='utf-8') as arq:
    dados2 = json.load(arq)
    print(dados2)