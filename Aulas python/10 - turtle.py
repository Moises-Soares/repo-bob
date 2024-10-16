# Tutorial Divertido de Python com Turtle para Crianças

# Primeiro, precisamos trazer a Turtle para o nosso programa. É como chamar um amigo para brincar!
import turtle

# Agora, vamos criar um espaço para a nossa tartaruga desenhar. É como abrir um livro de desenho.
tela = turtle.Screen()
tela.title("Aventuras da Tartaruga Artista")

# Vamos criar uma tartaruga e dar o nome de 'artista'. Ela será a nossa artista!
artista = turtle.Turtle()

# Agora, vamos ensinar a nossa tartaruga a desenhar um quadrado. É como seguir passos de dança!
def desenhar_quadrado(tamanho):
    for _ in range(4):        # Repetir 4 vezes porque um quadrado tem 4 lados.
        artista.forward(tamanho) # A tartaruga anda para frente.
        artista.right(90)        # Depois, ela vira 90 graus para a direita.

# A tartaruga também pode desenhar um círculo. Vamos mostrar como!
def desenhar_circulo(raio):
    artista.circle(raio)  # Dizemos o tamanho do círculo.

# Que tal desenhar uma estrela? Parece mágico, mas é fácil!
def desenhar_estrela(tamanho):
    for _ in range(5):        # Uma estrela tem 5 pontas, então repetimos 5 vezes.
        artista.forward(tamanho)
        artista.right(144)     # Ela vira 144 graus para fazer cada ponta da estrela.

# Vamos começar a desenhar!
# Primeiro, um quadrado.
desenhar_quadrado(100)

# Agora, movemos a tartaruga para não desenhar tudo no mesmo lugar.
artista.penup()           # Levantamos a caneta para ela não rabiscar enquanto se move.
artista.goto(-150, 100)   # Movemos ela para um novo lugar na tela.
artista.pendown()         # Colocamos a caneta no papel de novo para desenhar.

# Vamos fazer um círculo agora.
desenhar_circulo(50)

# Movendo a tartaruga outra vez para um bom lugar para desenhar a estrela.
artista.penup()
artista.goto(200, -150)
artista.pendown()

# E agora, uma estrela!
desenhar_estrela(100)

# Quando terminar de desenhar, podemos clicar na tela para fechar.
tela.exitonclick()
