print('===================== \n'
'  calculo da semana \n'
'=====================')
entrada = float(input('Quantos dias voçê trabalhou?:'))
preco = float(input('Qual o valor que voçê recebeu a cada dia ?:'))
dias = str(input('voçê recebe por mês ou por semana'.isupper))
resultado = entrada * preco 
match dias:
    case ('MÊS'):
        print('[]'.format(dias))