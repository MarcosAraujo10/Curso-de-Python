texto = "Curso de Python"

setimaPosicaoTexto = texto[6]
print(setimaPosicaoTexto)

textoCurso = texto[0:5]
print(textoCurso)

textoPython = texto[9:15]
print(textoPython)

#Contar o número de caracteres dentro do texto
qtdChar = len(texto)
print(f"Na frase temos {qtdChar} caracteres")

#Contar um número específico de letras dentro do texto
qtdLetrasO = texto.count("o")
print(f"Na frase temos {qtdLetrasO} letras o")

#Identifica a posição aonde inicia uma palavra
palavra = "Python"
posicaoPalavra = texto.find(palavra)
print(f"A palavra {palavra} inicia na posição {posicaoPalavra}")

#Identificação se existe a  palavra no texto
verificaPalavra = palavra in texto
print(f" a palavra {palavra} está no texto ? {verificaPalavra}")
