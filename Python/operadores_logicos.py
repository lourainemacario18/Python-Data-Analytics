print(True and True and True) #resultado verdadeiro
print(True and False and True) #resultado Falso
print(False and False and False) #resultado Falso
print(True or True or True) #resultado verdadeiro
print(True or False or False) # resultado verdadeiro
print(False or False or False) #resultado falso

# and = e
# or = ou
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
