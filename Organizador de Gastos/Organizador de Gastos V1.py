
# Variáveis e acumuladores
ali = 0
edu = 0
transp = 0
lazer = 0
div = 0
total = 0
maior_valor = 0
menor_valor = 0
desc_maior = ''
desc_menor = ''

# Cabeçalho
print('=' * 30)
print('ORGANIZADOR DE GASTOS'.center(30))
print('=' * 30)

num = int(input('Quantos gastos deseja cadastrar? '))

for c in range(1, num + 1):
    print('=' * 20, '{}º GASTO'.format(c), '='*20)
    print('[1] Alimentação \n [2] Educação \n [3] Transporte \n [4] Lazer \n [5] Outro')
    categoria = int(input('Categoria do Gasto: '))
    print('=' * 20)
    nome = str(input('Descrição do gasto: ')).strip()
    print('=' * 20)
    valor = float(input('Valor do Gasto: '))
    if categoria == 1:
        ali += valor
    elif categoria == 2:
        edu += valor
    elif categoria == 3:
        transp += valor
    elif categoria == 4:
        lazer += valor
    elif categoria == 5:
        div += valor
    total += valor
 
    if c == 1:
        maior_valor = valor
        menor_valor = valor
        desc_maior = nome
    else:
        if valor > maior_valor:
            maior_valor = valor
            desc_maior = nome
        if valor < menor_valor:
            menor_valor = valor
            desc_menor = nome 
media = total / num


print('=' * 30)
print('TOTAL DE GASTOS'.center(30))
print('Você gastou: {:.2f}'.format(total))
print('Sua média de gastos foi de {:.2f}'.format(media))
print('O seu maior gasto foi de {:.2f} com {}'.format(maior_valor, desc_maior))
print('O seu menor gasto foi de {:.2f} com {}'.format(menor_valor, desc_menor))
print('=' * 30)

print('Você gastou {:.2f} com alimentação.'.format(ali))
print('Você gastou {:.2f} com educação.'.format(edu))
print('Você gastou {:.2f} com Transporte.'.format(transp))
print('Você gastou {:.2f} com lazer.'.format(lazer))
print('Você gastou {:.2f} com gastos diversos.'.format(div))
                
    