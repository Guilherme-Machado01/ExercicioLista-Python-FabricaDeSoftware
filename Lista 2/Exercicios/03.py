# Crie um programa que receba dois números e mostre qual deles é o maior.

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

if(num1 > num2):
    print(f"{num1} é maior que  {num2}")
else:
    print(f"{num2} é maior que {num1}")