'''''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''''
#Solução Exercício 3
vetor=[]
while True:
    try:
        valor = float(input("Digite o valor de faturamento de hoje: "))
        vetor.append(valor)
    except ValueError:
        print("Por favor, insira um número válido.")
        continue
    loop = input('Deseja inserir mais valores? (S/N): ')
    if loop.lower() == 'n':
        break
if len(vetor) == 0:
    print("Nenhum valor de faturamento foi inserido.")
else:
    media = sum(vetor) / len(vetor)
    superior_media_mensal = sum(1 for x in vetor if x > media)
    print(f'Menor faturamento do mês: R${min(vetor):.2f}')
    print(f'Maior faturamento do mês: R${max(vetor):.2f}')
    print(f'Em {superior_media_mensal} dias do mês, o valor de faturamento diário foi superior à média mensal de R${media:.2f}')