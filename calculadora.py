num1 = int(input("digite o valor :"))
num2 = int(input("digite o valor :"))
operação = input ("digite a operação:")

match operação:
 case "+":
    res = num1 + num2
 case "-":
    res = num1 - num2
 case "*":
    res = num1 * num2
 case "/":
    res = num1 / num2
print(f"resultado é igual a {res}")