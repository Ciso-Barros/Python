# Exercício de fixação 6: Crie um programa que solicite ao usuário dois números e a operação que deseja executar entre eles. Mostre o resultado dessa operação no formato: num1 op num2 = resultado.


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
op = input("Qual operação deseja realizar ( + - * / )? ")
result = 0
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    op = "erro"
if op == "erro":
    print("Operação inválida!")
else:
    print(num1,op,num2,"=",result)
