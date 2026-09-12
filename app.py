# Sistema de Desconto Progressivo
# Autora: Emnauelly Nicolly

# ENTRADA
# solicita o valor total da compra:
valor_compra = float(input("Digite o valor total da compra: R$"))

# PROCESSAMENTO
# verifica qual desconto deve ser aplicado:
if valor_compra < 200:
    percentual_desconto = 5

elif valor_compra < 300:
    percentual_desconto = 10

else:
    percentual_desconto = 15

# calcula o valor do desconto:
valor_desconto = valor_compra * percentual_desconto / 100

# calcula o valor do desconto:
valor_final = valor_compra - valor_desconto

#SAÍDA
# exibe os resultados para o usuário
print("\n--- RESULTADO DA COMPRA---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"dESconto aplicado: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")
