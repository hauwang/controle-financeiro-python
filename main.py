"""
Sistema de Controle Financeiro Pessoal
Autor: Andrews Soares
Descrição:
Aplicação em Python que permite cadastrar renda, gastos e gerar
um resumo financeiro com base no percentual de gastos.
"""

from time import sleep

print('============================= \33[33mSISTEMA DE CONTROLE FINANCEIRO PESSOAL\33[m ===============================')
sleep(1)
print('\33[30m=-'*50)
print('''\33[34mEste sistema ajuda você a gerenciar suas finanças pessoais, permitindo o cadastro
de sua renda mensal e seus gastos. Com base nesses dados, o sistema fornecerá um resumo financeiro.''')
print('\33[30m=-'*50)
sleep(2)
renda = None
gasto = None
def validar():
    global renda, gasto
    while True:
        try:
            numero = int(input('''\33[36mESCOLHA UMA OPÇÃO:\33[m
\33[34m1 - Cadastrar Renda
2 - Cadastrar Gastos
3 - Ver resumo financeiro
4 - Sair\33[m
\33[35mDigite o número da opção desejada: \33[m'''))
            sleep(0.4)
            if numero not in [1, 2, 3, 4]:
                print('\33[31mOpção inválida. Tente novamente.\33[m')
                sleep(0.5)
                continue

        except ValueError:
            print('\33[31mOpção inválida. Tente novamente.\33[m')
            sleep(1)
            continue
        
        if numero ==1:
            while True:
                try:
                    renda = float(input('\33[35mDigite o valor da renda R$ \33[m'))
                    if renda <= 0:
                     print('\33[31mErro: a renda deve ser maior que zero. Tente novamente.\33[m')
                    else:
                        print(f'\33[32mRenda de R${renda:.2f} cadastrada com sucesso!\33[m')
                        break
                except ValueError:
                    print('\33[31mErro: digite um número válido.\33[m')
                    continue
        elif numero == 2:
           while True:
                try:
                    gasto = float(input('\33[35mDigite o valor do gasto R$ \33[m'))
                    if gasto < 0:
                        print('\33[31mErro: gasto não pode ser negativo.\33[m')
                    else:
                        print(f'\33[32mGasto de R${gasto:.2f} cadastrado!\33[m')
                        break
                except ValueError:
                    print('\33[31mDigite um número válido.\33[m')

        elif numero == 3:    
            if renda is None or gasto is None:
                print('\33[31mRESUMO FINANCEIRO NÃO DISPONÍVEL, CADASTRE RENDA E GASTOS PRIMEIRO.\33[m')
                sleep(1)
                continue
                
            atual = (gasto / renda) * 100
            if atual >= 100:
                print(f'\33[31mCUIDADO! VOCÊ ESTÁ GASTANDO MAIS DO QUE GANHA! VOCÊ ESTÁ COM {atual:.2f}% DE GASTOS EM RELAÇÃO À RENDA. DIMINUA SEUS GASTOS EM {atual - 65}% PARA MANTER UM ORÇAMENTO SAUDÁVEL.\33[m')
                sleep(2)           
            elif atual <= 65:
                print(f'\33[32mPARABÉNS! VOCÊ ESTÁ GERENCIANDO BEM SEU DINHEIRO! VOCÊ ESTÁ COM {atual:.2f}% DE GASTOS EM RELAÇÃO À RENDA. MANTENHA SEUS GASTOS ABAIXO DE 65% PARA UM ORÇAMENTO SAUDÁVEL.\33[m')
                sleep(2)
            else:
                print('\33[33mVOCÊ ESTÁ PRÓXIMO DO LIMITE DE GASTOS SAUDÁVEIS. TENTE MANTER SEUS GASTOS ABAIXO DE 65% DA RENDA.\33[m')
                sleep(2)
            opçao = input('\33[35mDeseja limpar os dados e cadastrar novos valores: \33[m')
            if opçao.lower() in ['sim', 's']:
                renda = None
                gasto = None
                print('\33[32mDados limpos com sucesso! Você pode cadastrar novos valores.\33[m')
                sleep(1)
                continue
            else:
                print('\33[32mMantendo os dados atuais.\33[m')
                sleep(1)


        elif numero == 4:
            print('\33[32mSaindo do sistema. Até logo!\33[m')
            break
validar()

    
