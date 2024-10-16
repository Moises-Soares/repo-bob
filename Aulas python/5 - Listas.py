# Bem-vindos ao Tutorial de Listas em Python!

# O que é uma lista?
# Uma lista é como uma coleção de coisas, como uma caixa de brinquedos. 
# Podemos colocar coisas lá dentro, tirar coisas, ou olhar para as coisas lá dentro.

# Exemplo 1: Criando uma lista
# Vamos fazer uma lista de frutas.
frutas = ["maçã", "banana", "laranja"]
print("Eu tenho estas frutas:", frutas)

# Exemplo 2: Adicionando itens à lista
# Vamos adicionar 'uva' à nossa lista.
frutas.append("uva")
print("Agora eu tenho estas frutas:", frutas)

# Exemplo 3: Acessando um item da lista
# Vamos ver qual é a segunda fruta.
print("A segunda fruta é:", frutas[1])  # Lembra-te, começamos a contar do 0!

# Exemplo 4: Removendo um item da lista
# Vamos tirar a 'banana' da lista.
frutas.remove("banana")
print("Depois de comer a banana, eu tenho:", frutas)

# Exemplo 5: Usando um ciclo com listas
# Vamos ver todas as frutas que temos, uma de cada vez.
for fruta in frutas:
    print("Eu tenho uma", fruta)

# Agora tenta tu! Cria a tua própria lista de coisas favoritas e usa um ciclo para mostrar cada uma delas.

# As listas são muito úteis para guardar e organizar coisas no nosso código!
