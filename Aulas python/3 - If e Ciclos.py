# Olá, jovens programadores! Hoje vamos aprender sobre como tomar decisões e repetir tarefas em Python. Vamos lá!

# 1. Tomando Decisões com if, else, e elif
# Às vezes, um programa precisa escolher o que fazer. É como escolher entre chocolate e baunilha!

# Exemplo 1: Usando if
# Vamos imaginar que a tua idade é uma chave para um clube secreto!
idade = 10
if idade >= 10:
    print("Bem-vindo ao clube dos 'Dez ou Mais'!")

# Exemplo 2: Usando if e else
# E se não tiveres 10 anos? Temos uma mensagem diferente para ti.
if idade < 10:
    print("Desculpa, ainda não tens 10 anos!")
else:
    print("Bem-vindo ao clube!")

# Exemplo 3: Usando if, elif, e else
# E se quisermos ser mais específicos?
if idade < 10:
    print("Ainda és muito jovem.")
elif idade == 10:
    print("Tens exatamente 10 anos, que legal!")
else:
    print("Uau, já tens mais de 10 anos!")

# Agora tenta tu! Escreve um código que diz algo especial para a tua idade.

# 2. Repetindo Tarefas com for e while
# E se quisermos fazer algo várias vezes? Usamos ciclos!

# Exemplo 4: Usando o ciclo for
# Vamos contar até 5.
for numero in range(5):
    print("Número", numero + 1)

# Exemplo 5: Usando o ciclo while
# Contar enquanto o contador for menor que 5.
contador = 0
while contador < 5:
    print("Contador é", contador)
    contador = contador + 1

# Tenta fazer um ciclo for para contar de 1 a 10.
# E um ciclo while para contar de 10 até 1.

# 3. Controlando os Ciclos com break e continue
# Às vezes, queremos parar um ciclo ou pular uma parte dele.

# Exemplo 6: Usando break
# Vamos contar até 10, mas parar no 5.
for i in range(10):
    if i == 5:
        break
    print(i)

# Exemplo 7: Usando continue
# Vamos contar até 10, mas pular os números pares.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Experimenta! Tenta usar break para parar um ciclo e continue para pular partes de um ciclo.

# Parabéns! Agora sabes como fazer programas que tomam decisões e repetem tarefas.
# Lembra-te, a prática leva à perfeição. Continua a programar e a divertir-te!