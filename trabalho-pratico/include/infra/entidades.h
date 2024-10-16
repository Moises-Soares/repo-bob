
#ifndef ENTIDADES_H
#define ENTIDADES_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <glib.h>


// enumeração para tipo de subscrição, i.e., normal ou premium
typedef enum{
    NORMAL,
    PREMIUM, 
    INVALIDO
} TipoSubscricao;

 // enumeração para tipo de artista, i.e., individual ou grupo musical.

 typedef enum{
    INDIVIDUAL,
    GRUPOMUSICAL
} TipoArtista;

//estrutura para armanezar os dados das músicas
typedef struct{
    int idMusica;
    int idArtista;
    char *tituloMusica;
    int duracaoMusicaEmSegundos;
    int anoLancamento;
    char *generoMusica;
    char *letraMusica;
} Musicas;

//estrutura para armanezar os dados dos users
typedef struct{
    int idUser;
    char *emailUsers;
    char *nomeUser;
    char *apelidoUser;
    GDate dataNascimentoUser;        //yyyy-mm-dd
    char *paisRegisto;
    TipoSubscricao tipoSubscricao;
    int *idMusicasGostadas;
    int numeroMusicasGostadas;
} Users;

//estrutura para armanezar os dados dos artistas
typedef struct{
    int idArtistas;
    char *nomeArtista;
    char *descricaoArtista;
    float profitPorReproducao;
    int *idConstituintesArtistas;
    int numeroConstituintesArtistas;
    char *nacionalidadeArtista; 
    TipoArtista tipoArtista;
    int duracaoDiscorgrafiaEmSegundos;            //querie2
} Artistas;

TipoSubscricao tipoDeSubscricao(char *subscricao);


#endif // ENTIDADES_H

