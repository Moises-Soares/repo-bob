# Bem-vindos ao Tutorial de Dicionários em Python!

# O que é um dicionário?
# Pensa num dicionário real, onde encontras a definição de uma palavra. 
# Em Python, um dicionário guarda coisas em 'pares': uma 'chave' e um 'valor'.

# Exemplo 1: Criando um dicionário
# Vamos fazer um dicionário sobre animais e os seus sons.
animais_sons = {"gato": "miau", "cão": "au au", "vaca": "muu"}

# Exemplo 2: Acessando valores
# Qual é o som que o gato faz?
som_do_gato = animais_sons["gato"]
print("O gato faz", som_do_gato)

# Exemplo 3: Adicionando novos pares
# E se quisermos adicionar mais animais?
animais_sons["leão"] = "roar"
print("O leão faz", animais_sons["leão"])

# Exemplo 4: Removendo pares
# Se não quisermos mais o som da vaca, podemos removê-lo.
del animais_sons["vaca"]
print("Depois de remover a vaca, temos:", animais_sons)

# Agora tenta tu! Cria um dicionário sobre o que quiseres e experimenta com ele.

# Os dicionários são ótimos para guardar informações que estão conectadas, como nomes e números de telefone!
