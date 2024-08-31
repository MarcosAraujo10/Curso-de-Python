#Atividade 1 



numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um número inteiro: "))
soma = numero1 + numero2
print(f' a soma é igual {soma}')


#Atividade 2

numeroBase=int(input("Digite um valor de 0 a 10: "))
sucessor = numeroBase + 1
antecessor = numeroBase - 1
print(f'O sucessor é igual a {sucessor} e o antecessor é igual a {antecessor}')

#Atividade 3
numeroDob=int(input("Digite um valor de 0 a 10: "))
dobro = numeroDob + numeroDob
print(f'O dobro do número é igual a {dobro}')

numeroTri=int(input("Digite um valor de 0 a 10: "))
triplo = numeroTri * 3
print(f'O triplo do número é igual a {triplo}')

numeroQua=int(input("Digite um valor de 0 a 10: "))
quadrado = numeroQua * numeroQua
print(f'O quadrado do número é igual a {quadrado}')

#Atividade 4
nota1 = 10
nota2 = 5
media = nota1 + nota2
final = media / 2
print(f'A nota do aluno é igual a {final}')

#Atividade 5
carteira=float(input("Digite o valor em dinheiro: R$ "))
dolar = 5
total = carteira / dolar
print (f'Ele pode comprar {total}  US$ ')

#Import math
import math
numero=int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
quadrado = numero * 4
raiz = math.sqrt(numero)
print(f"Propriedade do {numero} \n Dobro: {dobro} \n Triplo: {triplo} \n Quadrado: {quadrado}")