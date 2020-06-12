nome = input ("Digite o seu nome: ")
idade =int(input("Digite a sua idade: "))
sexo =str(input("Digite o seu sexo M/F "))
cnh =str(input("Possui CNH S/N? "))
eleitor =input("Possui titulo de eleitor S/N?.: ")
#teste 0
if idade < 18:
     print("É menor de idade.")
     #teste 1
     if idade == 16 or idade == 17:
          print("Pode solicitar o titulo de eleitor.")
     elif idade == 15:
          print("15 anos é uma idade linda.")
          #teste 2
          if sexo == "F" or sexo == "f":
               print("A", nome, "Tera um baile de debutante.")
          else:
               print("O", nome, "Tera uma festa com fast food.")
     elif idade == 13 or idade == 14:
          print(nome, "Já é adolescente.")

     elif idade < 13:
          print(nome, "Ainda é uma criança.")
#teste
else:
     print("É maior de idade.")
     if eleitor == "N" or eleitor == "n":
          print("Precisa solicitar o titulo de eleitor.")

     else:
          print("Deve votar na próxima eleição")
     if cnh == "N" or cnh == "n":
          print("Se quiser, pode tirar cnh.")
     else:
          print("Já possui CNH, Então pode dirigir.")

print("Obrigado", nome,"Volte sempre!")
