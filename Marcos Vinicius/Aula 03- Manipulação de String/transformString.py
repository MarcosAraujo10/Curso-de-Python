#Trocando uma palavra dentro de um texto
texto = 'Marcos Vinicius'
trocaPalavra =  texto.replace("Vinicius" , "Araujo")
print(trocaPalavra)

#Deixando todos os caracteres em maiúsculo
texto = "MaRcosViNicius@outlOOk.Com"
print(texto.upper())

textoMaisculo =  texto.upper()
print(textoMaisculo)

#Deixando todos os caracteres em minúsculo
textoMinusculo = texto.lower()
print(textoMinusculo)

#Deixando a primeira letra de cada palavra em Maiúsculo
texto = "meu primeiro curso no senai"
textoTitle = texto.title()
print(textoTitle)

#Deixando a primeira letra do texto em Maiúsculo
textoCapitalize = texto.capitalize()
print(textoCapitalize)

#Elimina espaços inúteis
texto = "     SENAI       "
textoStrip = texto.strip()
print(f'A palavra {textoStrip} tem {len(texto)} caracteres')

print(f'A palavra {textoStrip} tem {len(textoStrip)} caracteres')