#crie um programa que crie uma lista de armas para o heroi

print("os inimigos estão chegando voce encontrou varias armas em uma casa onde está escondido,escolha entre elas delas: ")
armas=["espada","faca","lanca","arco e flecha"]

for indice , item in enumerate(armas):
    print(f"{indice}-{item}")
quantidade=len(armas)
print(quantidade)
v=""
while v != "x":
    item_novo=input(" digite o item novo:  ")
    v=item_novo
    if v != "x":
        armas.append(item_novo)


print(f"Armas atuais: {armas}")
retire_arma=input("quer descartar alguma arma? ")
armas.remove(retire_arma)


