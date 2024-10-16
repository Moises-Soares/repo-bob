#include <stdio.h>
#include <glib.h>
#include "../infra/entidades.h"


void removeAspas(char *coluna);
Users *criaUtilizador(char *linha);
void carregaUtilizadores (GHashTable *hashTableUtilizadoresValidos, GList *listaUtilizadoresInvalidos);