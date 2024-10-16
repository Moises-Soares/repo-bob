# Bem-vindos ao Tutorial de Funções em Python!

# O que é uma função?
# Uma função é como uma pequena máquina que faz algo especial para nós.
# Nós damos algo a ela (chamamos isso de 'argumentos'), ela faz um trabalho e nos dá algo de volta.

# Exemplo 1: Uma função simples
# Vamos criar uma função que diz 'Olá' seguido pelo nome que lhe damos.
def dizer_ola(nome):
    print("Olá, " + nome + "!")

# Agora, vamos usar a função.
dizer_ola("Maria")
dizer_ola("João")

# Exemplo 2: Uma função que faz contas
# Esta função pega dois números, soma-os e devolve o resultado.
def somar_dois_numeros(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

# Vamos somar 5 e 3.
print("5 + 3 =", somar_dois_numeros(5, 3))

# Agora é a tua vez! Tenta criar uma função que multiplica dois números.

# Lembra-te: as funções ajudam-nos a não repetir o mesmo código várias vezes!
