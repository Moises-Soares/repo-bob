#include <stdio.h>
#include <glib.h>
#include "../../include/infra/entidades.h"
#include <unistd.h> 

// funçao que determina o tipo de subscrição
TipoSubscricao tipoDeSubscricao(char *subscricao)
{
    if (g_strcmp0(subscricao, "normal") == 0)
    {
        return NORMAL;
    }
    else if (g_strcmp0(subscricao, "premium") == 0)
    {
        return PREMIUM;
    }
    else
    {
        return INVALIDO;
    }

}
