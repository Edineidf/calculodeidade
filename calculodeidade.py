# Importando Biblioteca
from datetime import date
import datetime

# Coletando a data Atual e colocando na Variavel Hoje
hoje = date.today()
current_time = datetime.datetime.now()

# Solicitando a informacao por interacao do usuario
print('Calculo de vida, vivida')
nome = input('Informe seu Nome: ')
d1 = int(input('Em que dia Voce nasceu? '))
d2 = int(input('Qual mes de Nascimento? '))
d3 = int(input('Agora informe o ano que nasceu? '))

# Juntando a data
nascimento = date(d3, d2, d1)

# Subtraindo as datas
dif = hoje - nascimento

# Diferenca em dias
dia = dif.days

# Calculo
dias = dif.days
anos, dias = (dias // 365.25, dias % 365.25)
meses, dias = (dias // 30, dias % 30)

# Convertendo para Inteiro
anos = int(anos)
meses = int(meses)
dias = int(dias)

if anos >= 18:
    i = str('Maior de Idade')
else:
    i = str('Menor de Idade')


# Exibindo resultado na tela
print()
print('Data Nascimento Informada: {}/{}/{}'.format(d1, d2, d3))
print('Hoje é: {}/{}/{} sao {}h{}m'.format(hoje.day, hoje.month, hoje.year, current_time.hour, current_time.minute))
print('{}, voce é {} esta com {} anos, {} mes e {} dias de vida '.format(nome, i, anos, meses, dias))
print('Ate hoje passaram-se {} dias de vida.'.format(dia))
