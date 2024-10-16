#include <stdio.h>
#include <glib.h>
#include "../../include/infra/entidades.h"
#include <unistd.h> 
#include "../../include/infra/utils.h"

// TODO: Implementar a função de validação de email
//gboolean validarEmail(char *email)


gboolean validarUtilizador(Users *utilizador) {

     if (utilizador->tipoSubscricao == INVALIDO)
     {
        return FALSE;
     }

    if (!g_date_valid(&utilizador->dataNascimentoUser))
    {
        return FALSE;
    }
    // data nao pode ser depois de 2024/09/09
    if (g_date_compare(&utilizador->dataNascimentoUser, g_date_new_dmy(9, 9, 2024)) > 0)
    {
        return FALSE;
    }
    // validação do email
 //   if (!validarEmail(utilizador->emailUsers))
 //   {
   //     return FALSE;
    //}

    return TRUE;
}

// Função para processar os IDs das músicas gostadas e armazená-los como inteiros
void processarMusicasGostadas(Users *user, const char *coluna) {
    
    // remove os dois primeiros e os dois últimos caracteres da string "[ e ]"
    gchar *coluna_sem_brackets = g_strndup(coluna + 2, strlen(coluna) - 3); 

    // Divide a string com base nas vírgulas e espaços
    gchar **liked_songs_ids = g_strsplit(coluna_sem_brackets, ", ", -1);

    // Inicializa o GArray para armazenar os IDs das músicas como inteiros
    user->idMusicasGostadas = g_array_new(FALSE, FALSE, sizeof(int));

    // Converte cada ID de string para inteiro e o adiciona ao GArray
    for (int i = 0; liked_songs_ids[i] != NULL; i++) {

       // remover primeira plica e o S e a ultima plica
       gchar *liked_song_id = g_strndup(liked_songs_ids[i] + 2, strlen(liked_songs_ids[i]) - 2);

        int id = atoi(liked_song_id);
        g_array_append_val(user->idMusicasGostadas, id);
        user->numeroMusicasGostadas++;
    }

    g_strfreev(liked_songs_ids);
    g_free(coluna_sem_brackets);
}


// Função para criar um utilizador a partir de uma linha CSV
Users *criaUtilizador(char *linha)
{

    // Users *user = (Users *)malloc(sizeof(Users));
    Users *user = g_new(Users, 1); // Aloca memória para a struct Users
    // extrair conteúdo das colunas
    char **coluna = g_strsplit(linha, ";", -1);
    for (int i = 0; coluna[i] != NULL; i++)
    {
        removeAspas(coluna[i]);
    }

    user->idUser = atoi(coluna[0] + 1); // converter ID do utilizador de string para inteiro ignorando o primeiro caracter
   // printf("ID do utilizador: %d\n", user->idUser);
    // alocar memória para a string email e copiar email para struct
    user->emailUsers = g_strdup(coluna[1]);
   // printf("Email do utilizador: %s\n", user->emailUsers);

    user->nomeUser = g_strdup(coluna[2]);
   // printf("Nome do utilizador: %s\n", user->nomeUser);

    user->apelidoUser = g_strdup(coluna[3]);
   // printf("Apelido do utilizador: %s\n", user->apelidoUser);
    // preencher a struct passando de string para data usando glib
    char dataReformatada[11]; // Para armazenar a data reformulada
   // reformatarData(coluna[4], dataReformatada);
    //printf("Data original: %s\n", coluna[4]);
   // printf("Data reformatada: %s\n", dataReformatada);

// Confirmar que a data está no formato aaaa/mm/dd
if (coluna[4][4] == '/' && coluna[4][7] == '/') {
    g_date_set_parse(&user->dataNascimentoUser, coluna[4]);
}


    g_date_set_parse(&user->dataNascimentoUser, coluna[4]);

    // printf("Data de nascimento do utilizador: %d/%d/%d\n", g_date_get_year(&user->dataNascimentoUser), g_date_get_month(&user->dataNascimentoUser), g_date_get_day(&user->dataNascimentoUser));

    user->paisRegisto = g_strdup(coluna[5]);
   // printf("País de registo do utilizador: %s\n", user->paisRegisto);
    // Verificar se o utilizador é premium ou normal
    
    user->tipoSubscricao = tipoDeSubscricao(coluna[6]);
   // printf("Tipo de subscrição do utilizador: %d\n", user->tipoSubscricao);

    processarMusicasGostadas(user, coluna[7]);

    // Liberar o array de strings
    g_strfreev(coluna);

    return user; 
}

void carregaUtilizadores(GHashTable *hashTableUtilizadoresValidos, GHashTable *hashTableUtilizadoresInvalidos)
{

    // Buffer para armazenar o caminho atual
    char currentDir[1024];
    if (getcwd(currentDir, sizeof(currentDir)) != NULL) {
        printf("Diretório atual: %s\n", currentDir);
    } else {
        perror("Erro ao obter o diretório atual");
    }


    // variável para apontador para o ficheiro dos utilizadores
    FILE *ficheiroDadosUtilizadores = fopen("dataset/users.csv", "r");

    // Verifica se o ficheiro foi aberto corretamente
    if (ficheiroDadosUtilizadores == NULL)
    {
        perror("Erro ao abrir o ficheiro de utilizadores");
        return;
    }

    char linha[1000];

    // Lê a primeira linha (geralmente o cabeçalho) e imprime
    if (fgets(linha, sizeof(linha), ficheiroDadosUtilizadores) != NULL)
    {
        printf("Esta é a primeira linha:\n");
        printf("%s", linha); // Correção na impressão da linha
    }
    else
    {
        printf("Erro ao ler a primeira linha do ficheiro.\n");
        fclose(ficheiroDadosUtilizadores);
        return;
    }
    int numeroDeUtilizadores = 0;
    while (fgets(linha, sizeof(linha), ficheiroDadosUtilizadores) != NULL)
    {
        Users *utilizador;
        utilizador = criaUtilizador(linha);

        if (validarUtilizador(utilizador))
        {
            g_hash_table_insert(hashTableUtilizadoresValidos, &utilizador->idUser, utilizador);
        }
        else 
        {
            g_hash_table_insert(hashTableUtilizadoresInvalidos, &utilizador->idUser, utilizador);
        }

        numeroDeUtilizadores++;
        if (numeroDeUtilizadores % 10000 == 0)
        {
            printf("Numero de utilizadores carregados: %d\n", numeroDeUtilizadores);
        }

    }
    // Fecha o ficheiro
    fclose(ficheiroDadosUtilizadores);
    printf("numero de utilizadores : %d", numeroDeUtilizadores);
}