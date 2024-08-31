nomeCompleto = "Marcos Vinicius de Paulo Araujo"

primeiroNome = nomeCompleto[0:6]
print(f"Meu primeiro nome é {primeiroNome}")

ultimoNome = nomeCompleto[25: ]
print(f"Meu último nome é {ultimoNome}")

ultimoNome =  nomeCompleto[-6:]
print(ultimoNome)

#Quantidade de caracteres
qtdChar = len(nomeCompleto)
print(f"No nome temos {qtdChar} caracteres")

#Quantidades de letras a
qtdLetraA = nomeCompleto.count("a")
print(f"No nome temos {qtdLetraA} letras a")

#Aonde inicia o último nome
nomeF = "Araujo"
posicaoNome = nomeCompleto.find(nomeF)
print(f"O ultimo nome {nomeF} inicia na posição {posicaoNome} ")

#Verificar sobrenomes
nome1 = "Silva"
nome2 = "Souza"
nome3 = "Santos"
verificaNome = nome1 in nomeCompleto
print(f"o sobrenome {nome1} está no nome ? {verificaNome}")
print(f"o sobrenome {nome2} está no nome ? {verificaNome}")
print(f"o sobrenome {nome3} está no nome ? {verificaNome}")
