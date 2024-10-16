# Variável com o compilador que vamos usar, neste caso o gcc
# Certificar que gcc está instalado no sistema
CC = gcc

# Definição das bibliotecas que vamos usar
# Certificar que as bibliotecas estão instaladas no sistema
CFLAGS = $(shell pkg-config --cflags glib-2.0) # flag do compilador para incluir as bibliotecas
LIBS = $(shell pkg-config --libs glib-2.0) # flag para linkar a biblioteca glib-2.0

# Qual a pasta do projecto onde estão os ficheiros de cabeçalho
INCLUDE_DIR = include # pasta onde estão os ficheiros de cabeçalho
CFLAGS += -I$(INCLUDE_DIR)  # flag do compilador para incluir a pasta de cabeçalho

# Código fonte com o main do programa principal
SOURCE_CODE_PRINCIPAL = src/apresentacao/principal.c 

# Código fonte com o main do programa de testes
SOURCE_CODE_TESTES = src/apresentacao/testes.c

# Código fonte comum a ambos os programas
SOURCE_CODE_COMUM = $(wildcard src/dados/*.c src/infra/*.c src/logica/*.c)

# Pasta de destino para os binários/programas gerados 
TARGET_BIN_FOLDER = bin

# Ficheiro de destino para o executável do programa principal
PROGRAMA_PRINCIPAL_TARGET_BIN = $(TARGET_BIN_FOLDER)/$(basename $(notdir $(SOURCE_CODE_PRINCIPAL)))

# Ficheiro de destino para o executável do programa de testes
PROGRAMA_TESTES_TARGET_BIN = $(TARGET_BIN_FOLDER)/$(basename $(notdir $(SOURCE_CODE_TESTES)))

# na regra all colocamos o que fazer quando executamos o comando make sem argumentos
# No nosso caso executa a regra/target PROGRAMA_PRINCIPAL_TARGET_BIN
all: $(PROGRAMA_PRINCIPAL_TARGET_BIN)

# regra para criar a pasta de destino dos binários caso não exista
$(TARGET_BIN_FOLDER):
	@echo "Criando diretório de saída $(TARGET_BIN_FOLDER)"
	mkdir -p $(TARGET_BIN_FOLDER)

# Regra para compilar o programa principal
$(PROGRAMA_PRINCIPAL_TARGET_BIN): $(TARGET_BIN_FOLDER) $(SOURCE_CODE_PRINCIPAL) $(SOURCE_CODE_COMUM)
	@echo "Compilando o programa principal com $(CC)"
	@echo "Arquivo principal: $(SOURCE_CODE_PRINCIPAL)"
	@echo "Arquivos comuns: $(SOURCE_CODE_COMUM)"
	$(CC) -g $(SOURCE_CODE_PRINCIPAL) $(SOURCE_CODE_COMUM) $(CFLAGS) $(LIBS) -o $@
	@echo "Executável principal gerado em $(PROGRAMA_PRINCIPAL_TARGET_BIN)"

# Regra para compilar os testes, executar com "make tests"
tests: $(PROGRAMA_TESTES_TARGET_BIN)

# Regra para compilar o programa de testes
$(PROGRAMA_TESTES_TARGET_BIN): $(TARGET_BIN_FOLDER) $(SOURCE_CODE_TESTES) $(SOURCE_CODE_COMUM)
	@echo "Compilando o programa de testes com $(CC)"
	@echo "Arquivo principal: $(SOURCE_CODE_TESTES)"
	@echo "Arquivos comuns: $(SOURCE_CODE_COMUM)"
	$(CC) -g $(SOURCE_CODE_TESTES) $(SOURCE_CODE_COMUM) $(CFLAGS) $(LIBS) -o $@
	@echo "Executável de testes gerado em $(PROGRAMA_TESTES_TARGET_BIN)"

# Regra para executar o programa principal, executa com "make run"
run: $(PROGRAMA_PRINCIPAL_TARGET_BIN)
	@echo "Executando o programa principal..."
	./$(PROGRAMA_PRINCIPAL_TARGET_BIN)

# Clean rule to remove compiled executables
clean:
	@echo "Apagando os ficheiros executáveis na pasta bin"
	rm -rf $(TARGET_BIN_FOLDER)

.PHONY: all tests clean run
