#Desafio 01
texto = (input("Digite seu nome: "))
print(texto.upper())

print(texto.lower())

nomeSem = texto.replace ('' , '')
print(f'O nome {nomeSem} tem {len(nomeSem)} caracteres')

primeiroNome = texto.split()
print(primeiroNome[0])

#Desafio 02
cidade = (str(input("Digite o nome da cidade: ")))
splitString = cidade.split()
print(splitString[0])
print("Santo" in cidade)

#Desafio 03
nome = (str(input("Digite seu nome: ")))
print("Silva" in nome)

#Desafio 04
frase =  (str(input("Digite uma frase: ")))
qtdA = frase.count("a")
print(f"Na frase temos {qtdA} letras a")

inicio= frase.find("a")
print(f'A letra {"a"} se inicia na {inicio} posição')

ultima = frase.rfind("a")
print(f'a letra {"a"} termina na posição {ultima} ')

#Desafio 05
seuNome = (str(input("Digite seu nome: ")))
nomeUm = seuNome.split()[0]
ultimoNome = seuNome.split()[-1]
print(f"O primeiro nome é {nomeUm}")
print(f"O ultimo nome é {ultimoNome}")
