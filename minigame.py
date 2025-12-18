print('='*30)
print('FUJA DA FLORESTA DESCONHECIDA!')
print('dizem que aqui tem uma entidade a solta~')
print('='*30)
print('Você entrou numa floresta em plena noite e acaba se perdendo, mas acaba vendo uma trilha de pegadas, o que deseja fazer?')
escolha1 = input('[1] SEGUIR AS PEGADAS [2] DESVIAR DA PEGADAS ')
if escolha1 == "1":
    print('Você seguiu as pegadas e encontrou um abrigo, entrar nele?')
    escolha2 = input('[1]SIM [2]NÃO ')
    if escolha2 =='1':
        print('Você entrou no abrigo e encontrou suprimentos, mas num gesto rápido viu um vulto rápido, o vulto falou que queria te ver e parecia num tom arrependido')
        print('Abrir a porta ou se esconder? ')
        escolha3 = input('[1] ABRIR A PORTA [2] SE ESCONDER')
        if escolha3 == '2':
            print('Você se escondeu a tempo e o vulto arrombou a porta, vasculhou o abrigo inteiro mas não te encontrou, então acabou indo embora')
            print('GAME WIN!')
        elif escolha3 == '1':
            print('Você abriu a porta para o vulto, ele sorria para você, mas não de um jeito arrependido, ele disse que estava com fome...finalmente a refeição dele chegou')
            print('GAME OVER!')
        else:
            print('Número errado, por favor digite [1] para ABRIR A PORTA ou [2] para SE ESCONDER')
    elif escolha2 =='2':
        print('Você passou direto e acabou se perdendo, mas você se encontrou de frente com o vulto, ele sorriu para você antes de avançar')
        print('GAME OVER!')
    else:
        print('Número errado, por favor digite [1] para ENTRAR NO ABRIGO ou [2] para PASSAR DIRETO DO ABRIGO')
elif escolha1 =="2":
    print('Você desviou das pegadas e encontrou algo...ou alguém, mas antes que percebeu já estava tudo escuro demais...')
    print('GAME OVER!')
else:
    print('Número errado, por favor digite [1] para SEGUIR AS PEGADAS ou [2] para DESVIAR DAS PEGADAS')
print('='*30)