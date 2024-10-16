#include <stdio.h>
#include <glib.h>
#include "../../include/infra/utils.h"
#include <unistd.h> 


char * removeCaracteresNoInicioEFim(char *string, int inicio, int fim)
{
    gchar *stringSemCaracteres = g_strndup(string + inicio, strlen(string) - fim -1 );
    return stringSemCaracteres;
}

void removeAspas(char *coluna)
{
    size_t tamanho = strlen(coluna);
    if (coluna[0] == '"' && coluna[tamanho - 1] == '"')
    {
        // Se o primeiro e o último caracteres são aspas, removemos
        memmove(coluna, coluna + 1, tamanho - 2); // Remove aspas iniciais
        coluna[tamanho - 2] = '\0';               // Remove aspas finais
    }
}

