#%%
nome = input("Nome:")
idade = int(input("Idade:"))
peso = float(input("Peso:"))
altura = float(input("Altura:"))

valor_imc = peso/ (altura ** 2)
print(f"Recruta {nome}, o seu IMC calculado é : {round(valor_imc, 2)}")
# %%
#Se o IMC for menor que 18.5: Imprima "Status: Abaixo do peso".
#Se o IMC for maior ou igual a 18.5 E menor que 25: Imprima "Status: Peso ideal (Apto)".
#Se não for nenhum dos dois (ou seja, acima de 25): Imprima "Status: Sobrepeso".

if valor_imc < 18.5:
    print("Status: Abaixo do peso")
elif valor_imc >= 18.5 and valor_imc < 25:
    print("Status: Peso ideal (Apto)")
else:
    print("Status: Sobre peso")
# %%
