'''''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''''
#Solução Exercício 3
vetor=[22174.1664, 24537.6698,26139.6134, 0.0, 0.0, 26742.6612,0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563,
48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]
tamanholista = len(vetor) - 9
media = sum(vetor) / tamanholista
superior_media_mensal = sum(1 for x in vetor if x > media)
print(f'Menor faturamento do mês: R${min(vetor):.2f}')
print(f'Maior faturamento do mês: R${max(vetor):.2f}')
print(f'Em {superior_media_mensal} dias do mês o valor de faturamento diário foi superior à média mensal de R${media:.2f}')