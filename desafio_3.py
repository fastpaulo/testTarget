import json
values = []

############Abrindo arquivo JSON############
with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

############Calculo do maior e menor valorN############

def Numeros():
  for i in dados:
      if i['valor'] != 0.0:
        values.append(i['valor'])
  return values
Resultado = Numeros()    

print("O Maior Valor de Faturamento no Mes Foi: ",max(Resultado))
print("O Menor Valor de Faturamento no Mes Foi: ", min(Resultado))

###############Calculando Número de dias no mês em que o valor de faturamento diário foi superior à média mensal #########

Media = sum(Resultado)/ len(Resultado)
quantidade_dias = []
def Dias():
  for i in dados:
      if i['valor'] > Media:
        quantidade_dias.append(i['valor'])
  return quantidade_dias

Valor_dias = Dias()
print("Numero de dias no mes com faturamento superior ao mensal: ",len(Valor_dias))