'''''
4)Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

'''''
#Solução Exercício 4

vetor=[67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
faturamento = sum(vetor)
sp = (67836.43 * 100) / faturamento
rj = (36678.66 * 100) / faturamento
mg = (29229.88 * 100) / faturamento
es = (27165.48 * 100) / faturamento
outros = (19849.53 * 100) / faturamento
print(f'valor total mensal da distribuidora R${faturamento:.2f}')
print(f'SP teve {sp:.2f}% de representação')
print(f'RJ teve {rj:.2f}% de representação')
print(f'MG teve {mg:.2f}% de representação')
print(f'es teve {es:.2f}% de representação')
print(f'Outros tiveram {outros:.2f}% de representação')

