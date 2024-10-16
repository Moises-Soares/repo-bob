#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <glib.h>

typedef enum{
    NORMAL,
    PREMIUM,
    NAO_DEFINIDO
} TipoSubscricao;


typedef struct{
    int idUser;
    char *emailUsers;
    char *nomeUser;
    char *apelidoUser;
    GDate dataNascimentoUser;
    char *paisRegisto;
    TipoSubscricao tipoSubscricao;
    GArray *idMusicasGostadas;
    int numeroMusicasGostadas;
} Users;


// Função para criar um utilizador a partir de uma linha CSV
Users *criaUtilizador(char *linha);

// Função para libertar a memória alocada para um utilizador
void libertaUtilizador(Users *user);

// Função para criar uma string com a informação de um utilizador
char *utilizadorToString(Users *user);

// Função para verificar se o utilizador é válido
gboolean utilizadorValido(Users *user);

