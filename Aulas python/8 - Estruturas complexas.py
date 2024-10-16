# Bem-vindos ao Tutorial de Estruturas de Dados Complexas!

# Às vezes, precisamos guardar informações de maneiras mais complicadas. Vamos aprender como!

# 1. Listas Aninhadas
# Uma lista dentro de outra lista. Como uma caixa de tesouros com mais caixas dentro!

# Exemplo: Uma lista com diferentes tipos de doces
doces = [["gomas", "marshmallows"], ["chocolate", "bombons"]]

# Como encontrar 'marshmallows'?
print("Encontrei", doces[0][1], "na caixa!")

# 2. Dicionários Aninhados
# Um dicionário dentro de outro. Como um armário com várias gavetas, cada uma com seu rótulo!

# Exemplo: Um dicionário de receitas
receitas = {
    "bolo": {"farinha": 200, "açúcar": 100, "ovos": 2},
    "panqueca": {"farinha": 100, "leite": 150, "ovos": 1}
}

# Como encontrar a quantidade de farinha para fazer bolo?
print("Para fazer bolo, preciso de", receitas["bolo"]["farinha"], "gramas de farinha.")

# Agora tenta tu! Cria uma lista aninhada ou um dicionário aninhado sobre o que mais gostares.

# Com estas estruturas, podemos organizar muitas informações de maneira fácil!
