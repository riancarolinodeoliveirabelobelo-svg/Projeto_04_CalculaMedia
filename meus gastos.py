#quantos que voce gasta 

meu_salario = float(input("Meu salário dos sonhos:"))

gas = int(110)
luz = int(100)
agua = int(500) 
compra_do_mes = int(600)
internet = int(120)
iptu = int(700)
netflix = int(100)
ipva = int(4000)

despesas = gas + luz + agua + compra_do_mes + internet + iptu + netflix + ipva

sobra = meu_salario - despesas
print(f"Gastei: {despesas}  do meu salário, e sobrou: {sobra} para o mês.")