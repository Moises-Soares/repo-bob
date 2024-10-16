#include <stdio.h>
#include <glib.h>
#include "../../include/infra/entidades.h"
#include "../../include/dados/datasetUsuarios.h"

int main(int argc, char *argv[])
{
    // se não forem passados argumentos vai ler do stdin (terminal)
    FILE *origemDoInput = stdin;
    if (argc > 1)
    {
        // usamos isto para poder fazer debug na nossa máquina
        // se forem passados argumentos. vai abrir do ficheiro com nome que vem como parametro (input.txt configurado no launch.json do vscode)
        origemDoInput = fopen(argv[1], "r");
        printf("A abrir o ficheiro %s\n", argv[1]);
    }

    // hashTable para armazenar os utilizadores válidos
    // g_int_hash é a função de hash para inteiros
    // g_int_equal é a função para comparar inteiros
    GHashTable *hashTableUtilizadoresValidos = g_hash_table_new(g_int_hash, g_int_equal);

    // hashTable para armazenar os utilizadores inválidos
    GHashTable *hashTableUtilizadoresInvalidos = g_hash_table_new(g_int_hash, g_int_equal);



    carregaUtilizadores(hashTableUtilizadoresValidos, hashTableUtilizadoresInvalidos);

    // tota de utilizadores válidos
    int totalUtilizadoresValidos = g_hash_table_size(hashTableUtilizadoresValidos);

    // total de utilizadores inválidos
    int totalUtilizadoresInvalidos = g_hash_table_size(hashTableUtilizadoresInvalidos);

    printf("Total de utilizadores válidos: %d\n", totalUtilizadoresValidos);
    printf("Total de utilizadores inválidos: %d\n", totalUtilizadoresInvalidos);
    

    return 0;
}