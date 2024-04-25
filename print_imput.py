nome = input('Digite o seu nome :')
idade = input('Digite a sua idade')

print (nome,idade)
#exibe: (Louraine 18)

print (nome,idade, end-"...\n")
#exibe: (Louraine 18) quebra de linha (Louraine 18...)

print (nome,idade, sep ="#")
#exibe: (Louraine 18) quebra de linha (Louraine 18...) quebra de linha (Louraine#18)
