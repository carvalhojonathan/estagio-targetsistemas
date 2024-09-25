'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import json

with open('dados-questao3/dados.json', 'r') as file:
    dados = json.load(file)

faturamentos = []
for dia in dados:
    if dia['valor'] > 0:
        faturamentos.append(dia['valor'])

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_faturamento = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = 0
for valor in faturamentos:
    if valor > media_faturamento:
        dias_acima_da_media += 1

print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")