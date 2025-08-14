import datetime
ano = int(input('Que ano você quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):

    print(f'Esse ano é bissexto {ano}...')
else:
    print(f'Esse ano não é bissexto {ano}...')
