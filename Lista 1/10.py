# 10. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula
# de conversão é: C = 5.0∗(F −32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em
# Fahrenheit.


tempFahrenheit = float(input("Digite o valor da temperatura em fahrenheit: "))

celsius = 5.0 * (tempFahrenheit - 32.0 ) / 9.0

print("o valor de ",tempFahrenheit,"F em celsius é igual a: ",celsius,"°")  