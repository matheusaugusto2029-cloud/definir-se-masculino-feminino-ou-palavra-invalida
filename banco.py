#projeto de depositar, sacar e ver saldo no banco
#nome do banco ✔
#nome do cliente ✔
#idade do cliente se for menor que 18 não saca, não deposita e não ver saldo sem um maior presente ✔
#criar a quantidade minima de deposito ✔
#quantidade maxima de deposito ✔
#se usuario colocar mais que o limite de deposito no max e no mininimo da erro ✔
print("bem vindo ao banco LP")
print("A quantida minima para deposito é de 5.000$ ")
print("A quantidade maxima de deposito é de 50.000$")
nome_clinte= input("digite seu nome: ")
print(f"prazer, {nome_clinte} seja bem vindo ao banco LP!")
idade = int(input("digite sua idade:"))
if idade  >=18:
    print("confirmamos sua idade pode continuar a usar nosso sistema!")
else:
    print("lamentamos isso, mas você precisa de autorização de um responsavel para continuar!")
qntd_minima = 5000
qntd_maxima = 50000
deposito = int(input("digite quanto você irá depositar:"))
if deposito > qntd_maxima:
        print ("erro, ultrapassou o limite maximo!")
elif deposito < qntd_minima:
     print(" erro, valor muito abaixo do minimo!")
else:
     print("deposito realizado com sucesso!")