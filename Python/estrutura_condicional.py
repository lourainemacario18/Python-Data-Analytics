maior_idade = 18
idade_especial = 17

idade = int(input("Informe sua idade: "))

if idade > maior_idade:
    print ("Maior de idade, pode tirar a CNH")

if idade < maior_idade:
    print("Ainda nao pode tirar a CNH") 



if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH")
else: 
    print("Ainda nao pode tirar a CNH")


if idade >= maior_idade:
    print("Você já e maior de idade, pode tirar a CNH")
elif idade == idade_especial:
    print("Parabéns, já pode começar as aulas teóricas!")
else: 
    print("Que pena! Você ainda nao pode tirar a CNH")
