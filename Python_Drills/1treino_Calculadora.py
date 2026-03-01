# Treino de python

# Fazendo uma calculadora para o problema 

# Juliana vendeu seu patinete a 210 reais, o que era 70% do que ela havia pago.
# Por quanto ela deveria ter vendido para obter um lucro de 15%?

def calcular_venda_com_lucro(valor_venda_atual, porcentagem_atual, lucro_desejado):
    custo = (valor_venda_atual* 100) / porcentagem_atual #Descobrir o custo original
    valor_final = custo * (1 + (lucro_desejado/100))
    return valor_final

# Testando 
print(f"Valor ideal: R$ {calcular_venda_com_lucro(210,70,15)}")


#RESPOSTA Valor ideal: R$ 345.0