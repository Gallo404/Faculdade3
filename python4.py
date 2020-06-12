nomeFunc = input("Qual seu nome? ")
sexo = input("Você é M/F? ")
idade = int(input("Qual sua idade? "))
salAtual = float(input("Qual seu salario atual? "))
tempoFunc = float(input("A quanto tempo você é funcionário? "))
qntFilhos = int(input("Quantos filhos você tem? "))

if tempoFunc <= 2:
    reajuste = salAtual * 0.10
    bonus = qntFilhos * 100
if tempoFunc > 2 and tempoFunc < 5:
    reajuste = salAtual * 0.07
    bonus = qntFilhos * 200
else:
    reajuste = salAtual * 0.05
    bonus = qntFilhos * 300

if tempoFunc <= 2:
    reajuste = salAtual * 0.10
    bonus = qntFilhos * 100
    if tempoFunc <= 1:
        premio = "Receberá + 10 dias de férias"
    else:
        premio = "Receberá + 15 dias de férias"

elif tempoFunc > 2 and tempoFunc <= 5:
    reajuste = salAtual * 0.07
    bonus = qntFilhos * 200
    if idade >= 60:
        premio = "Plano de saúde gratuito"
    else:
        premio = "Plano odontológico"
else:
    reajuste = salAtual * 0.05
    bonus = qntFilhos * 300
    if sexo == 'F':
        premio = "Receberá 1 dia de spa"
    else:
        premio = "Receberá 1 almoço em churrascaria"

print(
    f"O (A) {nomeFunc} tem {idade} anos e é funcionário(a) há {tempoFunc} anos, receberá um bônus mensal de {bonus:.2f} por ter {qntFilhos} filho(s). \n Salário atual de {salAtual:.2f} foi reajustado para {reajuste:.2f}. Total de salário que {nomeFunc} irá receber é de {salAtual + reajuste + bonus}. O prêmio é receber {premio} ")