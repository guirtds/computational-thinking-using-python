#primeiro input
media_km_por_dia = float(input("Diga sua média de km rodados por dia útil: "))

#dados vindos do programa anterior
autonomia_em_km_por_L = 15

#calculando dados intermediários
media_km_mensal = media_km_por_dia * 20
media_litros_por_mes = media_km_mensal/autonomia_em_km_por_L

#segundo input
preco_por_litro = float(input("Diga quanto você pagou em reais por litro de gasolina:"))

valor_gasto_mensal = media_litros_por_mes * preco_por_litro

print("Você gasta, em média, por mês R$ {:.2f} com combustível.".format(valor_gasto_mensal))



