#%%
a = 1
b = 2 
print (a+b)
# %%
soma = a+b
print(soma)
# %%
#CRIAR UM DICIONARIO CHAMADO ALUNO
# 1. Criando o dicionário

aluno = {
    "nome": "Seu Nome",
    "curso": "Ciência de Dados",
    "semestre": 3 
}
print(aluno)

# 2. Exibindo apenas o curso
print(f"Estou focado no curso de: {aluno['curso']}")
# %%

#filtrando o dicionario de dados Imagine que você tem um mini dicionário 
# de estoque e precisa checar se um item está disponível.
#Objetivo:
#Crie um dicionário estoque = {"teclado": 10, "mouse": 0, "monitor": 5}.
#Use um if para verificar se a quantidade de "mouse" é maior que 0.
#Se for maior que 0, printe "Disponível". Se não, printe "Esgotado".

estoque = {
    "teclado": 11 ,
    "mouse" : 1000,
    "monitor" : 5
}

if estoque["mouse"] > 0 :
   print(f"A quantidade é : {estoque['mouse']}")
else :
   print("O valor de estoque esta zerado!")




# %%
